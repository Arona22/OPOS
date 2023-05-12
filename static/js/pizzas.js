$(document).ready(function() {
    $('#search-box').on('input', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        if (searchText === '') {
            // If the search box is empty, reload the page to show all results
            location.reload();
        } 
        else {
            // If the search box is not empty, send an AJAX request to get the filtered results
            $.ajax({
                'url': '/menu?search_filter=' + searchText,
                'type': 'GET',
                success: function(resp) {
                    if (resp.data.length === 0) {
                        // Display an error message if no search results are found
                        $('#pizzas').html(`<h1>No pizza named ${searchText}</h1>`);
                    } else {
                        // Generate HTML for the search results
                        var newHtml = resp.data.map(pizza => {
                            return `<div class="well-pizza">
                                        <a href="/menu/${pizza.id}" class="btn btn-primary" style="width: 18rem; background: rgba(118, 116, 116, 0.7);; border: gray;">
                                            <img src="/static/${pizza.firstImage }" class="card-img-top" alt="">
                                            <div class="card-body">
                                                <h5 class="pizza-title">${pizza.name}</h5>
                                                <p class="pizza-description">${pizza.description}</p>
                                                <div class="price-container">
                                                    <p>small:${pizza.price_small}kr</p>
                                                    <p>medium:${pizza.price_medium}kr</p>
                                                    <p>large:${pizza.price_large}kr</p>
                                                </div>
                                            </div>
                                        </a>
                                    </div>`
                        })
                        $('#pizzas').html(newHtml.join(''));
                    }
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            })
        }
    })
})


$(document).ready(function() {
    $('#category-select').on('change', function(e) {
        e.preventDefault();
        var categorySelect = document.querySelector('#category-select');
        var selectedRadio = categorySelect.querySelector('input[type=radio]:checked');
        var selectedLabel = categorySelect.querySelector('label[for="' + selectedRadio.id + '"]');
        var filter = selectedLabel.textContent;

        if (filter === 'All') {
            // If the search box is empty, reload the page to show all results
            location.reload();
        }
        else {
            $.ajax({
                'url': '/menu?category_filter=' + filter,
                'type': 'GET',
                success: function(resp) {
                    var newHtml = resp.data.map(pizza => {
                        return `<div class="well-pizza">
                                    <a href="/menu/${pizza.id}" class="btn btn-primary" style="width: 18rem; background: rgba(118, 116, 116, 0.7);; border: gray;">
                                        <img src="/static/${pizza.firstImage }" class="card-img-top" alt="">
                                        <div class="card-body">
                                            <h5 class="pizza-title">${pizza.name}</h5>
                                            <p class="pizza-description">${pizza.description}</p>
                                            <div class="price-container">
                                                <p>small:${pizza.price_small}kr</p>
                                                <p>medium:${pizza.price_medium}kr</p>
                                                <p>large:${pizza.price_large}kr</p>
                                            </div>
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

$(document).ready(function() {
    $('#success-outlined').on('change', function(e) {
        e.preventDefault();
        window.location.href = '/menu?order_by_name';
    })
})

$(document).ready(function() {
    $('#danger-outlined').on('change', function(e) {
        e.preventDefault();
        window.location.href = '/menu?order_by_price';
    })
})