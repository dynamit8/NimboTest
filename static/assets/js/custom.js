$(document).ready(function(){
    $("#addProductBySku #searchBySku").click(function(){
    	$("#addProductBySku .icon").addClass("active");
        $("#addProductBySku .overlayScreen").addClass("active");
        $("#searchBySku").addClass("active");
        $("#searchBySku").prop("placeholder","Add Products");
        $("#searchBySku").val('');
        $("#searchBySku").focus();

    });
    $("#searchBySku").blur(function(){
    	$("#addProductBySku .icon").removeClass("active");
        $("#addProductBySku .overlayScreen").removeClass("active");
        $("#searchBySku").removeClass("active");
        if(!$("#searchBySku").val()){
        	$("#searchBySku").val("Add Products");
        }
    });
});