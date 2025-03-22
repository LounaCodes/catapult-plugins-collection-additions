# Catapult Plugins Collection

Plugin collection to integrate with catapult launcher

# Plugins available

## Translator

### Usage

Just write the word tr, then the base language and the
language to translate, finally just add what you want translate.

Remember that for the translation to be executed you must add a trailing whitespace.

Format: `tr <Source language> <Target language> <Text><Trailing whitespace>`

Example: **tr en ru Hello World**

### Demo

![trans](https://user-images.githubusercontent.com/34254373/229021207-bafee2b3-d42a-485b-82d5-75e7789c215f.gif)

Installation:

```bash
curl https://raw.githubusercontent.com/CRAG666/catapult-plugins-collection/main/plugins/translator.py --output ~/.local/share/catapult/plugins/translator.py
```

## Hash

### Usage

Write the method with which you want to generate the hash.

Format: `<Method> <Text>`

Exaple: **sha256 Hello World!!**

### Available methods

- blake2b
- blake2s
- md5
- sha1
- sha224
- sha256
- sha384
- sha3224
- sha3256
- sha3384
- sha3512
- sha512
- shake128
- shake256

### Demo

![hash](https://user-images.githubusercontent.com/34254373/229021281-14cf928d-ccc1-48a2-96d9-c4f7b0cd22f3.gif)

Installation:

```bash
curl https://raw.githubusercontent.com/CRAG666/catapult-plugins-collection/main/plugins/hash.py --output ~/.local/share/catapult/plugins/hash.py
```

## WebSearch

### Usage

Just write `web` and then whatever search term you want to use on DuckDuckGo, or select one of the search suggestions from the list.
You can also just write out an URL and it will open in your default browser

Format: `web <search term>`

Example: **web was that the bite of 87?**
     or: **archlinux.org**

### Demo

![hash](https://github.com/LounaCodes/catapult-plugins-collection-additions/blob/main/web-search-demo.gif)
Installation:

```bash
curl https://raw.githubusercontent.com/LounaCodes/catapult-plugins-collection-additions/refs/heads/main/plugins/webSearch.py --output ~/.local/share/catapult/plugins/hash.py
```
change this when merged↑
