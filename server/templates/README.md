# Templates

These HTML files will be combined together to produce pages in order to prevent the need for multiple HTML files.

Look at `main.html`. This file contains 5 variables, shown in `{{ double_curly_braces }}`. Some are shown in
`{% curly_braces_and_precent_signs %}`. The simple double curly braces indicate that a python variable will be used
here, and curly braces with percent signs can be included here. The files are organized in this way so that the HTML is
maximally modular and neat.

An example:

```
render_template( "main.html", title="Test" )
```

This call will return a string that's like `main.html`, but with `{{ title }}` replaced with "Test".
