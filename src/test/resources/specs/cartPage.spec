@import common.spec


@objects
    empty-cart-head     css     .empty-cart.recommendation>h1
    bank-campaigns      id      bank-campaigns-container
    empty-cart-text     css     .empty-cart.recommendation>p
    empty-cart-icon     css     .empty-cart-icon-container


= Cart =
    @on desktop
        empty-cart-head:
            text is "Sepetin şu an boş."

        bank-campaigns:
            width ~ 1000px

        empty-cart-text:
            below empty-cart-head > 20px

        empty-cart-icon:
            above empty-cart-head 15 to 30px
