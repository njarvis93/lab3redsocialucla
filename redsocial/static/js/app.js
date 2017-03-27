/**
 * Created by Narvis Gil on 19/03/2017.
 */
var app = angular.module("RedSocialUCLA", ["ngRoute", "ngResource", "ngCookies"]);
app.config(function($routeProvider, $locationProvider, $interpolateProvider, $httpProvider) {
    $routeProvider
        .when("/",{
            controller: "CLogin"
        })
        .when("/canalprincipal/:pk",{
            templateUrl: "/templates/redtem/canal.html",
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
        .when("/administrador",{
            controller: "CAdministrador"
        })
        .when("/mis_canales",{
            controller: "CMisCanales",
            templateUrl: "/templates/redtem/mis_canales.html"
        })
        .when("/config", {
            controller: "Bichito"
        })
        .when("/seguidor",{
            controller: "Seguido"
        })
        .when("/listapost",{
            controller: "listpost"
        })

        ;
    $locationProvider.html5Mode({
      enabled: true,
      requireBase: false
    });
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.headers.common['X-CSRFToken'] = 'csrf_token|escapejs }}'
    }
);

app.run(
    function($http, $cookies) {
        $http.defaults.headers.post['X-CSRFToken'] = '{{ $cookies.csrftoken }}';
        // Add the following two lines
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
});