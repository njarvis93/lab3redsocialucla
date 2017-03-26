/**
 * Created by Narvis Gil on 19/03/2017.
 */
var app = angular.module("RedSocialUCLA");
app.factory("LoginResource", function($resource) {
    return $resource("http://localhost:8000/red/api_users/:pk",{pk: "@pk"}, {update: {method: "PUT"}});
});
app.factory("PostResource", function($resource) {
    return $resource("http://localhost:8000/red/all_post/:id", {id: "@id"}, {update: { method: "PUT"} });
});
app.factory("CanalResource", ['$resource',function($resource) {
    return $resource("http://localhost:8000/red/canales/:id", {id: "@id"}, {
        update: {
            method: "PUT",
        },
        query: {
            method: "GET",
            isArray: true
        }
    });
}]);
app.factory("ConfigResource", ['$resource', function($resource) {
    return $resource("http://localhost:8000/red/api_users/:id", {id: "@id"},{
        query: {
            method: "GET",
            isArray: true
        }
    });
}]);
app.factory("AreasResource", ['$resource', function($resource) {
    return $resource("http://localhost:8000/red/areas_conocimiento/all",{id: "@id"}, {
        query:{
            method: "GET",
            isArray: true
        }
    });
}]);

app.factory('Canal', ['$resource',function($resource) {
    return $resource('crud/canal/:id', { pk: '@pk'},{
        update: { method: "PUT", params:{ pk: "@pk" }}
    });
}]);