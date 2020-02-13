# Iota_address_tools

Useful tools geared towards iota seed and address manipulation.

##### seed_manager.py (deterministic iota seed generator)

##### vanity_address_manager.py (searches for custom addresses via brute force)

### Prerequisites

Tested on ubuntu 18.04.

Environment setup.

```
$ bash local_environment_setup.sh
```
```
Local environment setup successfully.
```

Activate environment.

```
$ source venv/bin/activate
```
```
(venv) $
```

Deactivate environment.

```
(venv) $ deactivate
```
```
$
```

## Up and running locally

These instructions will get you a copy of the project up and running on your local machine.

### Examples: seed_manager 

Help text.

```
(venv) $ python3 seed_manager.py help
```
```
Keywords:
help    Displays help text
random  Generates seed from random secret

Arguments:
(secret, seed_start=0, seed_stop=1, address_start=0, address_depth=1)
```

Generateing a seed with a random secret.

```
(venv) $ python3 seed_manager.py random
```
```
Secret: MCLRd4qGH8mBTOaFuWbgtdeWkpKbYD2asT9aRG5TrBiCCzwT1o2aFyWwnNxCAKQj
Seed 0: UWWKURGMOLQTUVMLHPAZTGLQ9MNAS9KQJAMVCJWDRTBNXFVEFMCQ9NWGRSENKXZTVULRJLPPKTNMZOJTE
Address 0: TMHPBPH9YPPNQISB9PERDITWYCXTAVIFOBVMLNKVQHRCDQCLMQC9KZRZMUNLTHRUMUTIRUXWCBLJWYQHCTIURKKLO9
```

Generating a seed from a secret.

```
(venv) $ python3 seed_manager.py secret_string
```
```
Seed 0: IOGUZJHRYMCV9KJYM9OCWFSQMMPHPMYQGXXYMIPZFNYT9SMXVRFNYODNHSQAHEMEFBHXOMJZRHHCFNIBF
Address 0: WVHLVAVASWRMGTFQAEDSROMDXMJZPVRCGPZYJPYUMPOYDFLGTRLBZYGDRCEDVGVYJWZ9FLOOYJEBJJBA9NNH9YDGBW
```

Generating a seed with specific index.

```
(venv) $ python3 seed_manager.py secret_string 1
```
```
Seed 1: IOGUZJHRYMCV9KJYM9OCWFSQMMPHPMYQGXXYMIPZFNYT9SMXVRFNYODNHSQAHEMEFBHXOMJZRHHCFNIBF
```

Generating multiple seeds.

```
(venv) $ python3 seed_manager.py secret_string 0 3
```
```
Seed 0: IOGUZJHRYMCV9KJYM9OCWFSQMMPHPMYQGXXYMIPZFNYT9SMXVRFNYODNHSQAHEMEFBHXOMJZRHHCFNIBF
Seed 1: UXPUOZDIHGZJCVAVMLBLTPHROTH9RMFJCIUSTHEAZHPZVTVXIMRRFITQGODVWUYISPDXHGOADHAPMPXCX
Seed 2: 9KQUQVMGBZHQVVSN9RZXYKKNQWIPLD9VGWKAYEDDPXKRBFDYFZOUGXUKWJCNDLVOISMCBIHXYSWEKYZSU
```

Generating multiple seeds with specific address index.
```
(venv) $ python3 seed_manager.py secret_string 0 3 1
```
```
Seed 0: IOGUZJHRYMCV9KJYM9OCWFSQMMPHPMYQGXXYMIPZFNYT9SMXVRFNYODNHSQAHEMEFBHXOMJZRHHCFNIBF
Address 1: QSVBWL9NHKYUKTXIBVRRTXHECNKZTGJTHKIQILYAHURFNICZWOBUJ9RADFHYQPEGHXM9FSNZWBZALS9DWJYVMYUVRX

Seed 1: UXPUOZDIHGZJCVAVMLBLTPHROTH9RMFJCIUSTHEAZHPZVTVXIMRRFITQGODVWUYISPDXHGOADHAPMPXCX
Address 1: SLFCJITDVPOPKJGTGJUIOTQYN9HAVYWPKANFWRXYKPGBAXPCLVCFVITTZKNOLCHJXHCKMEKOCOSSMSJHAH9XWSU9FW

Seed 2: 9KQUQVMGBZHQVVSN9RZXYKKNQWIPLD9VGWKAYEDDPXKRBFDYFZOUGXUKWJCNDLVOISMCBIHXYSWEKYZSU
Address 1: EVKLCKQJAPCSZUTJRRJMLKFXFNUXENIPCOTOBYDEOMKC9IFJMY9TJDXNANXSEHKGOXOISDC9XJDATGPCAFXZUYMYQW
```

Generating multiple seeds with multiple address indexes.
```
(venv) $ python3 seed_manager.py secret_string 0 3 0 3
```
```
Seed 0: IOGUZJHRYMCV9KJYM9OCWFSQMMPHPMYQGXXYMIPZFNYT9SMXVRFNYODNHSQAHEMEFBHXOMJZRHHCFNIBF
Address 0: WVHLVAVASWRMGTFQAEDSROMDXMJZPVRCGPZYJPYUMPOYDFLGTRLBZYGDRCEDVGVYJWZ9FLOOYJEBJJBA9NNH9YDGBW
Address 1: QSVBWL9NHKYUKTXIBVRRTXHECNKZTGJTHKIQILYAHURFNICZWOBUJ9RADFHYQPEGHXM9FSNZWBZALS9DWJYVMYUVRX
Address 2: QIWCFYRWGGXCXVLRTHQYOQDMDRRVTKLUBFYXFUGNOEIGSAGQ9VOKKHHLRRNPTGWLKFNFLMGUEAREJAGTBGMXYRZ9IX

Seed 1: UXPUOZDIHGZJCVAVMLBLTPHROTH9RMFJCIUSTHEAZHPZVTVXIMRRFITQGODVWUYISPDXHGOADHAPMPXCX
Address 0: GNMUWKTKOPUSEJUUFBZTUNPFACDSFFWRSKFTZZWQXTO9ZLSDWCCFKCXTLMDLFWUFLLKIAXYRTAYCTYZEWHUSWDBTD9
Address 1: SLFCJITDVPOPKJGTGJUIOTQYN9HAVYWPKANFWRXYKPGBAXPCLVCFVITTZKNOLCHJXHCKMEKOCOSSMSJHAH9XWSU9FW
Address 2: KRLEUPWCNUUE9FEKUPHKRVZIIZFMLADZWXDZWUFBDHAWBGWXZSTPHNHXQVLWNOBMZQKULSI9GCHJPTUDCPMHMFTBXX

Seed 2: 9KQUQVMGBZHQVVSN9RZXYKKNQWIPLD9VGWKAYEDDPXKRBFDYFZOUGXUKWJCNDLVOISMCBIHXYSWEKYZSU
Address 0: NQPAUWXRCCUUDKXQWSLRFGYQEFNFMHTXZIPGAYYF9MOEAVJZSLGMGVQFTCRPVUOVNJTV9EWWZPXHRENBWNDNWWR9QX
Address 1: EVKLCKQJAPCSZUTJRRJMLKFXFNUXENIPCOTOBYDEOMKC9IFJMY9TJDXNANXSEHKGOXOISDC9XJDATGPCAFXZUYMYQW
Address 2: YMCA9AXTDJIZJSNTCJGALBKQRLGRWVOMTWOYRVOCDDGJVXKRTKSISNOCQTJP9VKQIFCXQXUTFNLGBJFVXCJRJMXUR9
```

### Examples: vanity_seed_finder

Help text.
```
(venv) $ python3 vanity_address_manager.py help
```
```
Keywords:
help    Displays help text

Arguments:
(vanity_text, report_interval)
```

Vanity seed search silent.

```
(venv) $ python3 vanity_address_manager.py xx
```
```
Count:    368
Secret:   OaAwUYvwIeIfXhCeQWE7CJNhSDq5MsmkO16UioCUSL0UUWLdbuG6qcmY9OTLLkiM
Seed:     FDURCKJRUEKMIFNCESRHOUPJBVKNRIBURLLUZBFFT9LTNSWMWMDQOSJAAHDIHAMLGJMDTBQKVVIBOSZRD
Address:  XXCAAYIKAOFFLTNMIKRKFRKFJGUAQZYWMWVXXOEERUYFNZRKREIKDGJHIZWNKCHQHINQXRRBGRAJFUWLCSSLISYA9Z
```

Vanity seed search with progress reports.

```
(venv) $ python3 vanity_address_manager.py yy 100
```
```
Count:    0	 2020-02-08 22:18:12.894056
Count:    100	 2020-02-08 22:19:00.857304
Count:    200	 2020-02-08 22:19:48.946082
Count:    300	 2020-02-08 22:20:37.715318

Count:    383
Secret:   RSI2nXdVK0nFF7TwZEeV2JublML4ZpVeCFzFPvyZ0gYJXAucEkZvRiZ4mW3t01u7
Seed:     AOAFTLOJMDBTUQSJQCBUATMXAYEMOLXPNRGTGMVUJBAYYYVGIOLJLZHIHUHMINHHOTDIPBICJHTSMTJPJ
Address:  YYJMVMUNDMPCFTLP9RSELPCJPCEAVRMCEUKOAPKDQBQUSFLAKZTCSYVPILQCPINBLMBVSW9EN9UKVIRPCBCZIDKWKD
```

## Up and running with Docker

sub_seed_generator is available as a docker image for easy deployment.

Make sure you have Docker installed first. Instructions available [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/).

### Build images locally

The container is built upon an alpine image by default but you can enable ubuntu builds by editing the `docker-compose.yml` file.

```
(venv) $ docker-compose build
```
```
Successfully built cc90ac45738e
Successfully tagged seed_manager:alpine
```

View the containers.

```
$ docker images
```
```
REPOSITORY                TAG                 IMAGE ID            CREATED              SIZE
vanity_address_manager    alpine              47d85e7db405        About a minute ago   281MB
seed_manager              alpine              96c6d1c4b212        About a minute ago   281MB
iota_address_tools_base   alpine              4926fee19dc3        About a minute ago   281MB
```

The container accepts commands similar to previous examples.

```
(venv) $ docker-compose run --rm seed_manager:alpine secret_string
```
```
Seed 0: IOGUZJHRYMCV9KJYM9OCWFSQMMPHPMYQGXXYMIPZFNYT9SMXVRFNYODNHSQAHEMEFBHXOMJZRHHCFNIBF
Address 0: WVHLVAVASWRMGTFQAEDSROMDXMJZPVRCGPZYJPYUMPOYDFLGTRLBZYGDRCEDVGVYJWZ9FLOOYJEBJJBA9NNH9YDGBW
```

### Interactive disposable container

For maximum security you may wish to generate seeds from inside a disposable container which will leave no bash history
and delete all traces of itself when exited.

Drop into disposable container.

```
(venv) $ docker-compose run --rm --entrypoint sh seed_manager:alpine
```
```
#
```

Run commands similar to previous examples.

```
# python3 seed_manager.py secret_string
```
```
Seed 0: IOGUZJHRYMCV9KJYM9OCWFSQMMPHPMYQGXXYMIPZFNYT9SMXVRFNYODNHSQAHEMEFBHXOMJZRHHCFNIBF
Address 0: WVHLVAVASWRMGTFQAEDSROMDXMJZPVRCGPZYJPYUMPOYDFLGTRLBZYGDRCEDVGVYJWZ9FLOOYJEBJJBA9NNH9YDGBW
```

Exit container.

```
# exit
```
```
(venv) $
```

### Tests

Run tests.

```
(venv) $ python3 -m unittest
```
```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Run test for specific module.

```
$ python3 -m unittest tests/test_seed_manager.py
```
```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Author

* **derrend**
