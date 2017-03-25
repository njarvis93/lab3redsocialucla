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
app.controller("CMisCanales", ['$scope', 'CanalResource', '$window',function($scope, CanalResource, $window) {
    $scope.canales = CanalResource.query();
    $scope.canales.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
    $scope.id_can="";
    $scope.Redireccionar = function(dato){
        console.log(dato);
        $scope.canale = $scope.canales[dato-1];
        console.log($scope.canale);
        $window.location.href = "http://localhost:8000/red/canalprincipal?canal="+dato; 
        $scope.id_can = dato;
    }
   
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
