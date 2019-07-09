from torch.utils.data import DataLoader
from tensorboardX import SummaryWriter

import config
from utils.training import pass_epoch


def train(model, loss_fn, optimizer, scheduler, train_loader, val_loader):
    writer = SummaryWriter('runs')

    for epoch in range(config.epochs):
        model.train()
        train_loss, train_metrics = pass_epoch(
            model, loss_fn, train_loader,
            optimizer=optimizer, scheduler=scheduler, device=config.device
        )

        model.eval()
        val_loss, val_metrics = pass_epoch(
            model, loss_fn, val_loader,
            device=config.device
        )

        writer.add_scalar(f'loss/train', train_loss, epoch)
        writer.add_scalar(f'loss/val', val_loss, epoch)
        for metric_name, metric in train_metrics.items():
            writer.add_scalar(f'{metric_name}/train', metric, epoch)
        for metric_name, metric in val_metrics.items():
            writer.add_scalar(f'{metric_name}/val', metric, epoch)


if __name__ == '__main__':
    # Define instances
    model = build_instance(config.model).to(config.device)
    loss_fn = build_instance(config.loss_fn)
    optimizer = build_instance(config.optimizer, params=model.parameters())
    scheduler = build_instance(config.scheduler, optimizer=optimizer)
    train_dataset = build_instance(config.train_dataset)
    val_dataset = build_instance(config.val_dataset)
    train_batch_sampler = build_instance(config.train_batch_sampler)
    val_batch_sampler = build_instance(config.val_batch_sampler)

    # Define dataloaders
    train_loader = DataLoader(
        train_dataset,
        batch_sampler=train_batch_sampler,
        **config.train_dataset['loader']
    )
    val_loader = DataLoader(
        val_dataset,
        batch_sampler=val_batch_sampler,
        **config.val_dataset['loader']
    )


def build_instance(cfg, **kwargs):
    return cfg['cls'](**cfg['params'], **kwargs)
