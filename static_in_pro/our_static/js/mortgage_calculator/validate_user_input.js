$(document).ready(function(){


  $('#id_loan_value').keyup(function(event){
    // skip for arrow keys
    if(event.which >= 37 && event.which <= 40){
        event.preventDefault();
    }
    var $this = $(this);
    var num = $this.val().replace(/,/gi, "").split("").reverse().join("");

    var num2 = RemoveRougeChar(num.replace(/(.{3})/g,"$1,").split("").reverse().join(""));

    console.log(num2);


    // the following line has been simplified. Revision history contains original.
    $this.val(num2);
  });

  function RemoveRougeChar(convertString){
    if(convertString.substring(0,1) == ","){
        return convertString.substring(1, convertString.length)
    }
    return convertString;
  }


  var formDefaulter=function(){
    //Class to hold each form element
    var FormElement=function(element){
        var that=this;
        this.element=element;

        var initialVal=this.element.val();
        var isEdited=false;

        this.element.focus(function(){clearBox()});
        this.element.blur(function(){fillBox()});

        var clearBox=function(){
            if(!isEdited){
                that.element.val("");
                isEdited=true;
            }
        }
        var fillBox=function(){
            if(that.element.val()==""){
                that.element.val(initialVal);
                isEdited=false;
            }
        }
    }

    var add=function(elementId){
        new FormElement($('#'+elementId));
    }

    return{
        add:add
    }
  }();
  $(function(){
    formDefaulter.add('id_loan_value');
    formDefaulter.add('id_interest_rate');
    formDefaulter.add('id_loan_period');
});
});
