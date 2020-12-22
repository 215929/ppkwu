# vCardApi

vCardApi is a simple and intuitive API for browsing profesional offers and generating and downloading .vcf files with their details.


## Usage

The main endpoint of the API is:
`/vCardApi/profession=<profession>`
,where `<profession>` is the desired profession we want to look for

The other endpoint is used internally by the generated website and can also be accessed directly.
`/downloadVCard/name=<name>&&address=<address>&&phone=<phone>&&mail=<mail>`
It creates and starts a download of a vcf file with given data (`name`, `address`, `phone` and `mail`).


## Usage examples 

`/vCardApi/profession=hydraulik`

![example of web response](https://raw.githubusercontent.com/215929/ppkwu/master/ppkwu4/resources/vCardApiExample.png)

`/downloadVCard/name=FKC Krzysztof Chudobiński&&address=ul. Pabianicka 204, 93-402 Łódź&&phone=78  &&mail=fkc-bud@wp.pl`

BEGIN:VCARD
VERSION:3.0
ADDRESS:ul. Pabianicka 204\, 93-402 Łódź
EMAIL:fkc-bud@wp.pl
FN:FKC Krzysztof Chudobiński
TEL:78
END:VCARD
