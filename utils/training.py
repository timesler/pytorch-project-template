import time


class BatchLogger(object):

    def __init__(self, mode, calculate_mean=False):
        self.mode = mode
        self.calculate_mean = calculate_mean
        if self.calculate_mean:
            self.fn = lambda x, i: x / (i + 1)
        else:
            self.fn = lambda x: x

    def __call__(loss, metrics, i, n):
        track_str = f'\r{self.mode} |{i + 1:3d}/{n:<3}| '
        loss_str = f'loss: {self.fn(loss, i):9.4f} | '
        metric_str = ' | '.join(f'{k}: {self.fn(v, i):9.4f}' for k, v in metrics.items())
        print(track_str + loss_str + metric_str + '        ', end='')
        if i + 1 == n:
            print('')

    
class BatchTimer(object):
    """Batch timing class.

    Use this class for tracking training and testing time/rate per batch or per sample.
    
    Keyword Arguments:
        rate {bool} -- Whether to report a rate (batches or samples per second) or a time (seconds
            per batch or sample). (default: {True})
        per_sample {bool} -- Whether to report times or rates per sample or per batch.
            (default: {True})
    """

    def __init__(self, rate=True, per_sample=True):
        self.start = time.time()
        self.end = None
        self.rate = rate
        self.per_sample = per_sample

    def __call__(self, y_pred, y):
        self.end = time.time()
        elapsed = self.end - self.start
        self.start = self.end
        self.end = None

        if self.per_sample:
            elapsed /= len(y_pred)
        if self.rate:
            elapsed = 1 / elapsed

        return elapsed


def pass_epoch(
    model, loss_fn, loader, batch_metrics={'time': BatchTimer()},
    optimizer=None, scheduler=None, device='cpu'
):
    """Train or evaluate over a data epoch.
    
    Arguments:
        model {torch.nn.Module} -- Pytorch model.
        loss_fn {callable} -- A function to compute (scalar) loss.
        optimizer {torch.optim.Optimizer} -- A pytorch optimizer.
        loader {torch.utils.data.DataLoader} -- A pytorch data loader.
    
    Keyword Arguments:
        scheduler {torch.optim.lr_scheduler._LRScheduler} -- LR scheduler (default: {None})
        batch_metrics {dict} -- Dictionary of metric functions to call on each batch. The default
            is a simple timer. A progressive average of these metrics, along with the average
            loss, is printed every batch. (default: {{'time': iter_timer()}})
        device {str or torch.device} -- Device for pytorch to use. (default: {'cpu'})
        rolling_mean {bool} -- Whether or not to print losses and metrics for the current batch
            or rolling averages. (default: {False})
    
    Returns:
        tuple(torch.Tensor, dict) -- A tuple of the average loss and a dictionary of average
            metric values across the epoch.
    """
    
    mode = 'Train' if model.training else 'Eval '
    logger = Logger(mode, True)
    loss = 0
    metrics = {}
    for i_batch, (x, y) in enumerate(loader):
        x = x.to(device)
        y = y.to(device)
        y_pred = model(x)
        loss_batch = loss_fn(y_pred, y)

        if model.training:
            loss_batch.backward()
            optimizer.step()
            optimizer.zero_grad()

        for metric_name, metric_fn in batch_metrics.items():
            metrics[metric_name] = metrics.get(metric_name, 0) + metric_fn(y_pred, y)
        loss += loss_batch.detach().cpu()
        logger(loss, metrics, i_batch, len(loader))
    
    if model.training and scheduler is not None:
        scheduler.step()

    metrics = {k: v / (i_batch + 1) for k, v in metrics.items()}

    return loss, metrics
