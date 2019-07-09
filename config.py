import torch
from torch import optim, nn
import multiprocessing as mp

from utils import datasets, samplers, schedulers

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
num_workers = mp.cpu_count()

epochs = 100

model = dict(
    # cls=model.Model,
    # params=dict(
    #     # Named arguments for Model constructor
    # )
)

loss_fn = dict(
    # cls=nn.MSELoss,
    # params=dict(
    #     # Named arguments for loss constructor
    # )
)

optimizer = dict(
    # cls=optim.Adam,
    # params=dict(
    #     # Named arguments for optimizer constructor
    # )
)

scheduler = dict(
    # cls=schedulers.Scheduler,
    # params=dict(
    #     # Named arguments for Scheduler constructor
    # )
)

train_dataset = dict(
    # cls=datasets.Dataset,
    # params=dict(
    #     # Named arguments for Dataset constructor
    # ),
    # loader=dict(
    #     # Named arguments for DataLoader
    # )
)

val_dataset = dict(
    # cls=datasets.Dataset,
    # params=dict(
    #     # Named arguments for Dataset constructor
    # ),
    # loader=dict(
    #     # Named arguments for DataLoader
    # )
)

train_batch_sampler = dict(
    # cls=samplers.Sampler,
    # params=dict(
    #     # Named arguments for Sampler constructor
    # )
)

val_batch_sampler = dict(
    # cls=samplers.Sampler,
    # params=dict(
    #     # Named arguments for Sampler constructor
    # )
)
