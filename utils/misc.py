def print_model_parameters(model):
    print('\nModel parameters:')
    print(f'{"Parameter":25s}{"Shape":20s}Requires Grad')
    for n, p in model.named_parameters():
        print(f'{n:25s}{str(list(p.data.shape)):20s}{p.requires_grad}')
