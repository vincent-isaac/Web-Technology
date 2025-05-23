# Mathematical Calculations using JavaScript
## AIM:
To design a website to calculate the area of a triangle and volume of a cylinder using JavaScript.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Write JavaScript to perform calculations.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.


## PROGRAM:

### mathadd.html:
```
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>Area of triangle</title>
    <link rel="stylesheet" href="{% static 'css/mathadd.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
               AREA OF TRIANGLE
            </div>
            <div class="content">
                <form action="" method="GET">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_a">Base=</label>
                        <input type="text" name="value_a" id="value_a">
                    </div>
                    <div  class="forminput">
                        <label for="value_b">Height=</label>
                        <input type="text" name="value_b" id="value_b">
                    </div>                     
                    <div class="forminput">
                        <button type="button" name="button_add" id="button_add">Calulate</button>
                    </div>
                    <div class="forminput">
                        <label for="value_c">Area=</label>
                        <input type="text" name="value_c" id="value_c" readonly>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/mathadd.js"></script>
</body>

</html>
```

### mathvolume.html:
```
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>VOLUME OF THE CYLINDER</title>
    <link rel="stylesheet" href="{% static 'css/mathadd.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
                VOLUME OF THE CYLINDER
            </div>
            <div class="content">
                <form action="" method="GET">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_a">Base=</label>
                        <input type="text" name="value_a" id="value_a">
                    </div>
                    <div  class="forminput">
                        <label for="value_b">Height=</label>
                        <input type="text" name="value_b" id="value_b">
                    </div>                    
                    <div class="forminput">
                        <button type="button" name="button_add" id="button_add">Calculate</button>
                    </div>
                    <div  class="forminput">
                        <label for="value_c">Volume=</label>
                        <input type="text" name="value_c" id="value_c" readonly>
                    </div>                   
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/mathvolume.js"></script>
</body>

</html>
```

## JAVA SCRIPT:

### mathadd.js:
```
addBtn = document.querySelector('#button_add');

addBtn.addEventListener('click',function(e){

    txtA = document.querySelector('#value_a');
    txtB = document.querySelector('#value_b');
    txtC = document.querySelector('#value_c');

    let c ;

    c = 1/2 * parseFloat(txtA.value) * parseFloat(txtB.value) ;

    txtC.value = c;
});
```

### mathvolume.js:
```
result_button = document.querySelector('#button_add');

result_button.addEventListener('click', function(e){

    txta = document.querySelector('#value_a');
    txtb = document.querySelector('#value_b');
    txtc = document.querySelector('#value_c');
    
    let c;

    c = 22/7 * parseFloat(txta.value**2) * parseFloat(txtb.value);

    txtc.value = c;

});
```

## OUTPUT:
![output](./static/img/Aot.PNG)

![output](./static/img/Voc.PNG)

## VALIDATOR:
![output](./static/img/Aot-validator.PNG)

![output](./static/img/Voc-validator.PNG)


## RESULT:
Thus a website is designed for Area of trangle is hosted in the URL http://vincent.student.saveetha.in:8000/mathadd/
and Volume of cylinder is hosted in the URL http://vincent.student.saveetha.in:8000/mathvolume/ HTML code is validated.
