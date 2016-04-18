# Introduction #

In lieu of a formal document, we describe here the XKB format, suitable for lexing.


# Details #

An XKB file consists of sections that have the form
```
// comments can appear here.
one of more modifiers "mysectionname"
{
   // comments can appear here.
   include "somename"                 // comments can also appear here.
   name[somestring] = "sometext";
   key.type[someotherstring] = "someothertext";
   key <someotherstring> { [ somesymbol, someothersymbol, ... uptoEightSymbols ] };
   modifier_map someothertext { somesymbol, someothersymbol, ... uptoEightSymbols };
   // can also have multiples of the above.
};

// can have several sections as above.
```