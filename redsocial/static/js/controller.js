/**
 * Created by Narvis Gil on 19/03/2017.
 */
var app = angular.module("RedSocialUCLA");
app.controller("CPost", function($scope, PostResource) {
    $scope.posts = PostResource.query();
    console.log($scope.posts);
});
app.controller("CMisCanales", ['$scope', 'CanalResource' ,function($scope, CanalResource) {
    $scope.canales = CanalResource.query();
    $scope.canales.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
    console.log($scope.canales);
    /*var vm = this;
    vm.encabezado = "Canales";
    $scope.canales=[];
    CanalResource.query().$promise.then(function(data) {
        console.log('Succes: '+JSON.stringify(data));
        vm.canals = data;
        $scope.canales = JSON.stringify(data);
        console.log($scope.canales);
    }, function(reason) {
        console.log('ERROR: '+JSON.stringify(reason));
    });*/

    //console.log($scope.canales);
}]);
app.controller("CCanal", function($scope, $routeParams, CanalResource) {
    $scope.canal = CanalResource.get({id: $routeParams.id})
});