/**
 * Created by Narvis Gil on 19/03/2017.
 */
var app = angular.module("RedSocialUCLA");
app.controller("CPost", ['$scope', 'PostResource', function($scope, PostResource) {
    $scope.posts = PostResource.query();
    $scope.posts.$promise.then(function(data) {
        //console.log(JSON.stringify(data));
    });
    console.log($scope.posts);
}]);
app.controller("CMisCanales", ['$scope', 'CanalResource', '$window', 'Canal', 'AreasResource', function($scope, CanalResource, $window, Canal, AreasResource) {

    $scope.canales = CanalResource.query();
    $scope.canales.$promise.then(function(data) {
        //console.log(JSON.stringify(data));
    });
    $scope.id_can="";
    $scope.Redireccionar = function(dato){
        console.log(dato);
        $scope.canale = $scope.canales[dato-1];
        console.log($scope.canale);
        $window.location.href = "http://localhost:8000/red/canalprincipal?canal="+dato; 
        $scope.id_can = dato;
    };
    $scope.canals = Canal.query();
    var fecha_hoy = new Date();
    $scope.misareas = {
        model: null,
        opciones: AreasResource.query(),
        opcionSeleccionada:[-1]
    };
    var areas_cono = $scope.misareas.model;
    $scope.new_canal = new Canal({fecha_creacion: fecha_hoy.getFullYear()+"-"+fecha_hoy.getMonth()+"-"+fecha_hoy.getDate(), autor: 'user1', areas: areas_cono});

    $scope.Guardar = function() {

        $scope.new_canal.$save(function() {
            $scope.canals.push(new_canal);
        }).then(function() {
            $scope.CMisCanales();
            $scope.new_canal = new Canal();
        }).then(function() {
            $scope.errors=null
        }, function(rejection) {
                $scope.errors = rejection.data;
        })
    };

}]);
app.controller("CCanal", ['$scope', '$location','CanalResource',function($scope, $location, CanalResource) {
    var id_canal = $location.search().canal;
    console.log(id_canal);
    $scope.micanal = $scope.canales[id_canal];
    console.log($scope.micanal);
}]);
app.controller("CComentariosPorPost", ['$scope', 'ComentariosPorPostResource', function($scope, $routeParams, ComentariosPorPostResource) {
    $scope.comentarios = ComentariosPorPostResource.query();
    $scope.comentarios.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });

}]);
app.controller("Bichito",['$scope', 'ConfigResource', function($scope, ConfigResource) {
    $scope.usuarios = ConfigResource.query();
    $scope.usuarios.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    })
}]);
app.controller("AreasConocimiento", ['$scope', 'AreasResource', function($scope, AreasResource) {
    $scope.areas = AreasResource.query();
    $scope.areas.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
}]);