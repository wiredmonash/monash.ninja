$(document).ready(function() {

  $("#wired-btn").click(function() {
    $("#wired-head").toggleClass("hide");
  });

  $("#form").submit(function() {

    console.log("Posting... " + $("#code").val());

    console.log(JSON.stringify({code:"test"}));

    code = $("#code").val();
    if (code == "") {
      mark_error("Please enter a code.");
    } else {
    	$.ajax({

    		type: "POST",
    		url: "/get",
    		data: JSON.stringify({code: code}),
    		contentType: 'application/json;charset=UTF-8',
    		success: function(data) {
    			if(data.status == "error") {
    				mark_error("Invalid code.");
    			} else {
    				mark_success("Code valid :) Generating coupon...");
    			}
    			console.log(data.status);
    		}

    	});

    }

    event.preventDefault();

  });

  function reset_form() {
    $("#form").removeClass("successful error blank");
    $("#message").removeClass("alert-success alert-danger");
  };

  function mark_success(string) {
    reset_form();
    $("#message").html(string);
    $("#form").addClass("successful");
    $("#message").addClass("alert-success");
  }

  function mark_error(string) {
    reset_form();
    $("#message").html(string);
    $("#form").addClass("error");
    $("#message").addClass("alert-danger");
  }
});
