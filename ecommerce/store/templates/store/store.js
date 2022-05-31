/* Document.redyState beschreibt Ladezustand des document-Objektes */
if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}
/* Wenn man Löschbutton, Mengen-Input und Warenkorb Button betätigt, wird Aktion erzeugt durch click*/
/* Werden dann in Array gespeichert*/
function ready() {
    var removeCartItemButtons = document.getElementsByClassName('btn-danger')
    for (var i = 0; i < removeCartItemButtons.length; i++) {
        var button = removeCartItemButtons[i]
        button.addEventListener('click', removeCartItem)
    }

    var quantityInputs = document.getElementsByClassName('cart-quantity-input')
    for (var i = 0; i < quantityInputs.length; i++) {
        var input = quantityInputs[i]
        input.addEventListener('change', quantityChanged)
    }

    var addToCartButtons = document.getElementsByClassName('shop-item-button')
    for (var i = 0; i < addToCartButtons.length; i++) {
        var button = addToCartButtons[i]
        button.addEventListener('click', addToCartClicked)
    }

    document.getElementsByClassName('btn-purchase')[0].addEventListener('click', purchaseClicked)
}
/*"Jetzt kaufen" klicken und Einkauf abschließen*/
/* Fenster mit Weiterleitung wird angezeigt*/
function purchaseClicked() {
    alert('Sie werden weitergeleitet. Bitte auf "OK" klicken.')
    var cartItems = document.getElementsByClassName('cart-items')[0]
    while (cartItems.hasChildNodes()) {
        cartItems.removeChild(cartItems.firstChild)
    }
    updateCartTotal()
}
/* wenn Produkt aus Warenkorb gelöscht wird*/
/* neuer Preis und Mengen werden aktualisiert*/
function removeCartItem(event) {
    var buttonClicked = event.target
    buttonClicked.parentElement.parentElement.remove()
    updateCartTotal()
}
/* Wenn Anzahl eines Produkts im Warenkorb mit einem unzulässigen Zeichen/Zahl verändert wird*/
function quantityChanged(event) {
    var input = event.target
    if (isNaN(input.value) || input.value <= 0) {
        input.value = 1
    }
    updateCartTotal()
}
/*Wenn man dem Warenkorb ein Produkt hinzufügt*/
/*Titel, Preis und Bild werden in Variablen gespeichert*/
/*Funktion addItemToCart() wird aufgerufen*/
function addToCartClicked(event) {
    var button = event.target
    var shopItem = button.parentElement.parentElement
    var title = shopItem.getElementsByClassName('shop-item-title')[0].innerText
    var price = shopItem.getElementsByClassName('shop-item-price')[0].innerText
    var imageSrc = shopItem.getElementsByClassName('shop-item-image')[0].src
    addItemToCart(title, price, imageSrc)
    updateCartTotal()
}
/*Produkt wird im Array gespeichert*/
/*in Array wird überprüft, ob gleiches Produkt schon bereits im Warenkorb liegt*/
/*Wenn ja, Meldung -> Wenn nein, dann wird sie hinzugefügt*/
/*es wird bei jedem Produkt ein <div> erzeugt*/
function addItemToCart(title, price, imageSrc) {
    var cartRow = document.createElement('div')
    cartRow.classList.add('cart-row')
    var cartItems = document.getElementsByClassName('cart-items')[0]
    var cartItemNames = cartItems.getElementsByClassName('cart-item-title')
    for (var i = 0; i < cartItemNames.length; i++) {
        if (cartItemNames[i].innerText == title) {
            alert('Dieses Produkt wurde schon bereits hinzugefügt. Bitte ändern Sie die Anzahl des Produkts unten im Warenkorb.')
            return
        }
    }
    var cartRowContents = `
        <div class="cart-item cart-column">
            <img class="cart-item-image" style="margin-top: 10px; margin-left: 0px; margin-bottom: 10px; float: center;" src="${imageSrc}" width="100" height="100">
            <span class="cart-item-title">${title}</span>
       
        <span class="cart-price cart-column">${price}</span> </div>
        <div class="cart-quantity cart-column">
            <input class="cart-quantity-input" 
			style="width: 60px; margin-right: 50px; margin-left: -200; margin-left: -100; margin-left: -100px;" type="number" value="1">
            <button class="btn btn-danger" type="button">Löschen</button>
        </div>`
	/* Produkt wird der Liste hinzugefügt*/
    cartRow.innerHTML = cartRowContents
    cartItems.append(cartRow)
    cartRow.getElementsByClassName('btn-danger')[0].addEventListener('click', removeCartItem)
    cartRow.getElementsByClassName('cart-quantity-input')[0].addEventListener('change', quantityChanged)
}
/*Preise werden summiert und in der Variable "total" gespeichert*/
function updateCartTotal() {
    var cartItemContainer = document.getElementsByClassName('cart-items')[0]
    var cartRows = cartItemContainer.getElementsByClassName('cart-row')
	total = 0
    for (var i = 0; i < cartRows.length; i++) {
        var cartRow = cartRows[i]
        var priceElement = cartRow.getElementsByClassName('cart-price')[0]
        var quantityElement = cartRow.getElementsByClassName('cart-quantity-input')[0]
        var price = parseFloat(priceElement.innerText.replace('$', ''))
        var quantity = quantityElement.value
        total = total + (price * quantity)
    }
    total = Math.round(total * 100) / 100
    document.getElementsByClassName('cart-total-price')[0].innerText = '$' + total 

	}
