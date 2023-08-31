<script src="/static/js/jquery-3.6.4.js"></script>

$(document).ready(function(){
    function updateSummary() {
        let totalPrice = 0;
        let totalPayment = 0;
        let savingsAmount = 0;

        $('.quantity').each(function(index, input) {
            const itemInfoDiv = $(input).parent().parent();
            const originalPrice = parseFloat(itemInfoDiv.find('.price:nth-child(2) span').text());
            const discount = parseFloat(itemInfoDiv.find('.price:nth-child(3) span').text());

            const quantity = parseInt($(input).val());
            totalPrice += originalPrice * quantity;
            totalPayment += originalPrice * discount * quantity;
        });

        savingsAmount = totalPrice - totalPayment;

        $('#total').text(`¥${totalPrice.toFixed(2)}`);
        $('#savings').text(`¥${savingsAmount.toFixed(2)}`);
        $('#totalPayment').text(`¥${totalPayment.toFixed(2)}`);
    }

    $('.minusBtn').click(function() {
        const input = $(this).siblings('.quantity');
        if (parseInt(input.val()) > 0) {
            input.val(parseInt(input.val()) - 1);
            updateSummary();
        }
    });

    $('.plusBtn').click(function() {
        const input = $(this).siblings('.quantity');
        input.val(parseInt(input.val()) + 1);
        updateSummary();
    });

    $('.quantity').change(updateSummary);

    $('#payBtn').click(function() {
    const totalPayment = parseFloat($('#totalPayment').text().substring(1));
    let totalItems = 0;
    $('.quantity').each(function(index, input) {
        totalItems += parseInt($(input).val());
    });

    // create data object
    const data = {
        total_price: totalPayment,
        quantity: totalItems
    };

    // send post request
    $.ajax({
        url: `/cart/update/{{ g.user.user_id }}`, // replace 1 with actual cart_id if dynamic
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success: function(response) {
            console.log(response);
            location.href = "http://127.0.0.1:5000/payment/{{ g.user.user_id }}";
            alert(`Are you sure you want to purchase?\r
             The total amount of money needed to be spent: ¥${totalPayment.toFixed(2)}.\r
            The total number of items present in the shopping cart: ${totalItems}`);
        },
        error: function(error) {
            console.log(error);
        }
    });
});

    updateSummary();
});

