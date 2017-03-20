/**
 * Created by Narvis Gil on 19/03/2017.
 */
var app = angular.module("RedSocialUCLA", ["ngRoute", "ngResource"]);
app.config(function($routeProvider) {
    $routeProvider
        .when("/",{
            controller: "CLogin"
        })
        .when("/canalprincial",{
            controller: "CCanal"
        })
        .when("/crearcanal",{
            controller: "CCrearCanal"
        })
        .when("/perfil",{
            controller: "CPerfil"
        })
        .when("/miperfil",{
            controller: "CMiPerfil"
        })
        .when("/timeline",{
            controller: "CPost",
            templateUrl: "/templates/redtem/timeline.html"
        })
        .when("/timeline_privado",{
            controller: "CPostPrivado"
        })
        .when("/canalprincipal/:id",{
            controller: "CCanal",
            templateUrl: "/templates/redtem/canal.html"

        })
        .when("/administrador",{
            controller: "CAdministrador"
        })
        .when("/mis_canales",{
            controller: "CMisCanales",
            templateUrl: "/templates/redtem/mis_canales.html"
        })
});