def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)

"""
+------------------------------------------------------------------------+
+ code                                                call stack         +
+------------------------------------------------------------------------+
+ fact(3)                                         +--------------------+ +
+ if x == 1:                                      +        FACT        + +
+ else:                                           +--------------------+ +
+                                                 +    x    |    3     + +
+                                                 +--------------------+ +
+------------------------------------------------------------------------+
+ return x * fact(x-1)                            +--------------------+ +
+ if x == 1:                                      +        FACT        + +
+ else:                                           +--------------------+ +
+                                                 +    x    |    2     + +
+                                                 +--------------------+ +
+                                                 +        FACT        + +
+                                                 +--------------------+ +
+                                                 +    x    |    3     + +
+                                                 +--------------------+ +
+------------------------------------------------------------------------+
+ return x * fact(x-1)                            +--------------------+ +
+ if x == 1:                                      +        FACT        + +
+                                                 +--------------------+ +
+                                                 +    x    |    1     + +
+                                                 +--------------------+ +
+                                                 +        FACT        + +
+                                                 +--------------------+ +
+                                                 +    x    |    2     + +
+                                                 +--------------------+ +
+                                                 +        FACT        + + 
+                                                 +--------------------+ +
+                                                 +    x    |    3     + +
+                                                 +--------------------+ +
+------------------------------------------------------------------------+
+ return 1                                        +--------------------+ +
+                                                 +        FACT        + +
+                                                 +--------------------+ +
+                                                 +    x    |    2     + +
+                                                 +--------------------+ +
+                                                 +        FACT        + +
+                                                 +--------------------+ +
+                                                 +    x    |    3     + +
+                                                 +--------------------+ +
+------------------------------------------------------------------------+
+ return x * fact(x-1) # x=2, fact(x-1)=1         +--------------------+ +
+                                                 +        FACT        + +
+                                                 +--------------------+ +
+                                                 +    x    |    3     + +
+                                                 +--------------------+ +
+------------------------------------------------------------------------+
+ return x * fact(x-1) # x=3, fact(x-1)=1*2                              +
+------------------------------------------------------------------------+
"""

