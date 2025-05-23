

addBtn = document.querySelector('#button_add');

addBtn.addEventListener('click',function(e){

    txtA = document.querySelector('#value_a');
    txtB = document.querySelector('#value_b');
    txtC = document.querySelector('#value_c');

    let c ;

    c = 1/2 * parseFloat(txtA.value) * parseFloat(txtB.value) ;

    txtC.value = c;
});