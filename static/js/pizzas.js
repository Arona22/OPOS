$(document).ready(function() {
    $('#search-box').on('input', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        if (searchText === '') {
            // If the search box is empty, reload the page to show all results
            location.reload();
        } else {
            // If the search box is not empty, send an AJAX request to get the filtered results
            $.ajax({
                'url': '/menu?search_filter=' + searchText,
                'type': 'GET',
                success: function(resp) {
                    var newHtml = resp.data.map(pizza => {
                        return `<div class="well-pizza">
                                    <a href="/menu/${pizza.id}" class="btn btn-primary" style="width: 18rem; background: rgba(118, 116, 116, 0.7);; border: gray;">
                                        <img src="/static/${pizza.firstImage }" class="card-img-top" alt="">
                                        <div class="card-body">
                                            <h5 class="pizza-title">${pizza.name}</h5>
                                            <p class="pizza-description">${pizza.description}</p>
                                        </div>
                                    </a>
                                </div>`
                    })
                    $('#pizzas').html(newHtml.join(''));
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            })
        }
    })
})