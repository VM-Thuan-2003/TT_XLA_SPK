def _make_layer(num_blocks, stride):
    strides = [stride] + [1]*(num_blocks-1)
    print(strides)
    layers = []
    for stride in strides:
        layers.append(1)
    return layers


print(_make_layer(2, 2))
