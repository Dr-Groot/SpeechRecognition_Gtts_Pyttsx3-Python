[< PREVIOUS](np_intro.md) || [NEXT >](np_ndarray.md)

# GETTING STARTED WITH ENVIRONMENT

Standard Python distribution doesn't come bundled with NumPy module. A lightweight alternative is to install NumPy using popular Python package installer, pip.

In terminal:
```
pip install numpy
```

In anaconda:
```
conda install numpy
```

If already have check version using __version__ attribute:
```python
print(numpy.__version__)
```


Upgrading NumPy:
```
pip install --upgrade numpy
```

## Importing and Alias

Once NumPy is installed, import it in your applications by adding the **import** keyword:
```python
import numpy
```

NumPy is usually imported under the np alias.

>  In Python alias are an alternate name for referring to the same thing.

Create an alias with the as keyword while importing:
```python
import numpy as np
```

Now, we can refer NumPy package as **np** instead of **NumPy**

<br />

[HOME](README.md)

[< PREVIOUS](np_intro.md) || [NEXT >](np_ndarray.md)
