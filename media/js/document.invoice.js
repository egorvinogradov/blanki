Blanki.Invoice = Blanki.extend(Blanki.Base);

Blanki.Invoice.prototype.init = function(){
    this.auth = new Blanki.Auth();
    this.auth.init();
};
