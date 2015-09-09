$(document).ready(function() {

  $("#wired-btn").click(function() {
    $("#wired-head").toggleClass("hide");
  });

  $("#form").submit(function() {

    console.log("Posting... " + $("#code").val());

    console.log(JSON.stringify({code:"test"}));

    code = $("#code").val();
	sid = $("#sid").val();
    if (code == "" && sid == "") {
      mark_error("Please enter a code and a student ID.");
	} else if (code == ""){
	  mark_error("Please enter a code");
	} else if (sid == "") {
	  mark_error("Please enter a student ID.");
	} else {
    	$.ajax({

    		type: "POST",
    		url: "/get",
    		data: JSON.stringify({code: code, student_id: sid}),
    		contentType: 'application/json;charset=UTF-8',
    		success: function(data) {
    			if(data.status == "error") {
    				mark_error("Invalid code.");
    			} else {
    				mark_success("You've won a prize! Come along to our <a href='https://www.facebook.com/events/430433180499149/'>AGM</a> on Monday 14 September to collect it!'");
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
