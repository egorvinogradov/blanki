Blanki.Promo = Blanki.extend(Blanki.Base);

Blanki.Promo.prototype.init = function(){
    this.auth = new Blanki.Auth();
    this.auth.init();
};
