
let allProducts = [];

async function loadProducts() {
    try {
        const response = await fetch("/api/products");
        const data = await response.json();

        if (data.success) {
            allProducts = data.products;
            loadCategories();
            updateStats();
            applyFilters();
        }

    } catch (error) {
        console.error("Error loading products:", error);
    }
}

function displayProducts(products) {
    const container = document.getElementById("productContainer");

    container.innerHTML = "";

    products.forEach(product => {
        container.innerHTML += `
            <div class="product-card">
                <img src="${product.thumbnail}"
                     alt="${product.title}"
                     class="product-image">

                <h3>${product.title}</h3>
                <p>Price: $${product.price}</p>
                <p>Category: ${product.category}</p>
                <p>Rating: ${product.rating}</p>
                <p>Stock: ${product.stock}</p>
            </div>
        `;
    });
}



function loadCategories() {
    const categoryFilter = document.getElementById("categoryFilter");

    const categories = [...new Set(
        allProducts.map(product => product.category)
    )];

    categories.forEach(category => {
        categoryFilter.innerHTML += `
            <option value="${category}">${category}</option>
        `;
    });
}

function applyFilters() {
    const searchText = document.getElementById("searchInput").value.toLowerCase();
    const selectedCategory = document.getElementById("categoryFilter").value;

    const filteredProducts = allProducts.filter(product => {
        const matchesSearch = product.title.toLowerCase().includes(searchText);

        const matchesCategory =
            selectedCategory === "all" ||
            product.category === selectedCategory;

        return matchesSearch && matchesCategory;
    });

    displayProducts(filteredProducts);
}

document.getElementById("categoryFilter").addEventListener("change", applyFilters);

document.getElementById("searchInput").addEventListener("input", applyFilters);


function updateStats() {
    const total = allProducts.length;

    const totalPrice = allProducts.reduce(
        (sum, product) => sum + product.price, 0
    );

    const totalRating = allProducts.reduce(
        (sum, product) => sum + product.rating, 0
    );

    const averagePrice = total > 0 ? totalPrice / total : 0;
    const averageRating = total > 0 ? totalRating / total : 0;

    document.getElementById("totalProducts").textContent = total;

    document.getElementById("averagePrice").textContent =
        "$" + averagePrice.toFixed(2);

    document.getElementById("averageRating").textContent =
        averageRating.toFixed(2);
}

loadProducts();
