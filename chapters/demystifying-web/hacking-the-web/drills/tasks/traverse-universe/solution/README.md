# Name: Traverse universe

## Vulnerability

Path Traversal in URL path.

## Exploit

Check the source code if `index.html`.
There you'll find the following line:

```html
<!--<script>var _0x5c09=['dot-php','earth\x20','log','slash\x20','dot-dot-slash\x20','flag\x20','NASA\x20'];(function(_0xe916b7,_0x5c0933){var _0x34f1b0=function(_0x4a989c){while(--_0x4a989c){_0xe916b7['push'](_0xe916b7['shift']());}};_0x34f1b0(++_0x5c0933);}(_0x5c09,0xa1));var _0x34f1=function(_0xe916b7,_0x5c0933){_0xe916b7=_0xe916b7-0x0;var _0x34f1b0=_0x5c09[_0xe916b7];return _0x34f1b0;};var algf=_0x34f1('0x4')+_0x34f1('0x1')+_0x34f1('0x3')+'moon\x20'+'slash\x20'+_0x34f1('0x6')+_0x34f1('0x3')+_0x34f1('0x5')+_0x34f1('0x0');console[_0x34f1('0x2')](algf);</script>-->
```

Executing the script in the console reveals the path to the flag:

```plaintext
dot-dot-slash earth slash moon slash NASA slash flag dot-php
```

Open this URL in your browser: `http://141.85.224.102:8015/panetarium/../earth/moon/NASA/flag.php`.
