$(document).ready(function (){
    $( function() {
        $( "#startdate" ).datepicker({
            altField: "#startdatepicker"
        });
        $( "#enddate" ).datepicker({
            altField: "#enddatepicker"
        });
        $( "#date" ).datepicker({
            altField: "#datepicker"
        });
    } );

    $("#btn1").click(function(){
        console.log($("#startdatepicker").val());
        console.log($("#enddatepicker").val());
        alert($("#timetemplate").val());
    });
    
    $("#tmpdiario").hide();
    
    $("#timetemplate").change(function(){
        var tmp = $("#timetemplate").val();
        if (tmp == "Diario"){
            $("#tmpsemanal").hide();
            $("#tmpdiario").show();
        }
        if (tmp == "Semanal"){
            $("#tmpsemanal").show();
            $("#tmpdiario").hide();
        }
    })
    

});



