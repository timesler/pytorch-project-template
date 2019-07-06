def log(mode, i, n, metrics):
    track_str = f'\r{mode} |{i + 1:3d}/{n:<3}| '
    metric_str = ' | '.join(f'{k}: {v / (i + 1):9.4f}' for k, v in metrics.items())
    print(track_str + metric_str + '        ', end='')


def pass_epoch(trader, loss_fn, scheduler, phase):
    loss = []
    metrics = {}
    for i_batch, (x, y) in enumerate(phase):
        y_pred = trader(x)
        metrics_batch, *timeseries = loss_fn(y_pred, y[:, trader.y_loc])

        mode = 'Eval '
        if trader.training:
            mode = 'Train'
            metrics_batch['Loss'].backward()

        metrics = {k: metrics.get(k, 0) + v for k, v in metrics_batch.items()}
        log(mode, i_batch, len(phase), metrics)
    
    if trader.training:
        scheduler.optimizer.step()
        scheduler.optimizer.zero_grad()
        scheduler.step()
    
    print('')

    metrics = {k: v / (i_batch + 1) for k, v in metrics.items()}

    return metrics, timeseries


def print_model(model):
    print('\nModel parameters:')
    print(f'{"Parameter":25s}{"Shape":20s}Requires Grad')
    for n, p in model.named_parameters():
        print(f'{n:25s}{str(list(p.data.shape)):20s}{p.requires_grad}')
