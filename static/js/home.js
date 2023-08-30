function showLoanValue() {
    var loanRequired = document.getElementById("loan_required");
    if (loanRequired !== null) {
      var loanValue = parseFloat(loanRequired.value); // Parse the value as a floating-point number
      var currency = "INR"; // Use the currency code for Indian Rupee
      var numberFormat = new Intl.NumberFormat("en-IN", {
        style: "currency",
        currency: currency
      });
      document.getElementById("loan_value").innerHTML = numberFormat.format(loanValue);
    }
  }
  
  // Attach the event listener to the range slider after the element has been loaded
  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("loan_required").addEventListener("input", showLoanValue);
  });
  