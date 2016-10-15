# Python Zekr pack reader
This is a reader for Quran translation Zekr packs.


## Install
   
```sh
    $ sudo pip install zekrpack_reader
```

## Usage
```python    
    >>> from zekrpack_reader import TranslationModel
    >>> tm = TranslationModel("./example.zip")
    >>> props = tm.translation_properties()
    >>> props["country"] 
    TR
    >>> lines = tm.translation_lines(props)
    >>> len(lines)
    6236
```        
     
## License
GPL
       
