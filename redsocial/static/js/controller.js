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
app.controller("CMisCanales", ['$scope', 'CanalResource', function($scope, CanalResource) {
    $scope.canales = CanalResource.query();
    $scope.canales.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
    console.log($scope.canales);
}]);
app.controller("CCanal", ['$scope', 'CanalResource' ,function($scope, $routeParams, CanalResource) {
    $scope.canal = CanalResource.get({id: $routeParams.id});
    $scope.canal.$promise.then(function(data) {
        console.log(data);
    });
}]);
app.controller("CComentariosPorPost", ['$scope', 'ComentariosPorPostResource', function($scope, $routeParams, ComentariosPorPostResource) {
    $scope.comentarios = ComentariosPorPostResource.query();
    $scope.comentarios.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });

}]);
app.controller("Bichito",['$scope', 'ConfigResource', function($scope, ConfigResource) {
    nEditar = {};
    $scope.usuarios = ConfigResource.query();
    $scope.usuarios.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    })


}]);
