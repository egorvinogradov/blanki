Blanki.Auth = function(){

    // TODO: Сделать родительский base-модуль.
    // TODO: Наследоваться всегда от него
    // TODO: Сделать метод selectorsToNodes

    this.settings = {
        selectors: {
            body: '.promo',
            container: '.auth',
            button: '.auth-button',
            dropdown: {
                login: '.auth-login',
                registration: '.auth-registration'
            },
            link: {
                login: '.auth-link__login',
                registration: '.auth-link__register'
            }
        },
        classes: {
            opened: 'auth_opened'
        }
    };
};

Blanki.Auth.prototype.init = function(){

    // TODO: использовать selectorsToNodes

    this.els = {};
    this.els.body = $(this.settings.selectors.body); // TODO: создавать this.els.body в base-модуле автоматически
    this.container = $(this.settings.selectors.container);
    this.els.button = $(this.settings.selectors.button);

    this.els.dropdown = {};
    this.els.dropdown.login = $(this.settings.selectors.dropdown.login);
    this.els.dropdown.registration = $(this.settings.selectors.dropdown.registration);

    this.els.link = {};
    this.els.link.login = $(this.settings.selectors.link.login);
    this.els.link.registration = $(this.settings.selectors.link.registration);

    // TODO: расширить jquery.on, передавать 3-м аргументом контекст

    this.els.button.on('click', $.proxy(function(){
        this.els.dropdown.login.addClass(this.settings.classes.opened);
    }, this));

    this.els.link.registration.on('click', $.proxy(function(){
        this.els.dropdown.login.removeClass(this.settings.classes.opened);
        this.els.dropdown.registration.addClass(this.settings.classes.opened);
    }, this));

    this.els.link.login.on('click', $.proxy(function(){
        this.els.dropdown.login.addClass(this.settings.classes.opened);
        this.els.dropdown.registration.removeClass(this.settings.classes.opened);
    }, this));

    this.els.body.on('click keydown', $.proxy(function(event){
        if ( !$(event.target).parents().is(this.settings.selectors.container) || event.which === 27 ) {
            this.els.dropdown.login.removeClass(this.settings.classes.opened);
            this.els.dropdown.registration.removeClass(this.settings.classes.opened);
        }
    }, this));
};
