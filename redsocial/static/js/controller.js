/**
 * Created by Narvis Gil on 19/03/2017.
 */
var app = angular.module("RedSocialUCLA");
app.controller("CPost", ['$scope', 'PostResource', 'Post', function($scope, PostResource, Post) {
    $scope.posts = PostResource.query();
    $scope.posts.$promise.then(function(data) {
        //console.log(JSON.stringify(data));
    });
    var fecha_hoy = new Date();
    console.log(fecha_hoy.getHours()+":"+fecha_hoy.getMinutes()+":"+fecha_hoy.getMinutes());
    $scope.allposts = Post.query();
    $scope.tipospost = {
        model: null,
        availableOptions: [
            {id: '1', name: 'Publico'},
            {id: '2', name: 'Privado'}
        ]
    };
    $scope.id_canales = {
        model: [],
        opcionSeleccionada:[]
    }
    console.log($scope.posts);
    $scope.Guardar = function(new_post){
        console.log("--"+new_post.autor+"--"+new_post.contenido+"---"+$scope.usuario);
        if(!new_post.pk){
            var nuevo_post = new Post();
            //nuevo_post.id = new_post.id;
            nuevo_post.tipo = new_post.tipo;
            nuevo_post.contenido = new_post.contenido;
            nuevo_post.fecha_creacion = fecha_hoy.getFullYear()+"-"+fecha_hoy.getMonth()+"-"+fecha_hoy.getDate();
            nuevo_post.hora_creacion = fecha_hoy.getHours()+":"+fecha_hoy.getMinutes()+":"+fecha_hoy.getMinutes();
            nuevo_post.autor = $scope.usuario;
            nuevo_post.id_canal = []
            if(new_post.aux_canal!== null) {
                nuevo_post.id_canal[0] = new_post.aux_canal;
            }
            nuevo_post.$save(function() {
                $scope.allposts.push(nuevo_post);
            }).then(function () {
                console.log("Post agregado");
                $scope.new_post = new Post();
            }).catch(function (errors) {
                $scope.errors = null
                console.log(errors);
            });
        }else{
            alert("El id ya existe!");
            new_post.$update();
            $scope.new_post.descripcion = " ";
            $('#modal_post').modal('hide');
        }
    };
    $scope.remove = function(new_post) {
        if(confirm("¿Desea eliminar esta publicación y todo su contenido?")) {
            new_post.$remove(function () {
                var idx = $scope.allposts.indexOf(new_post);
                $scope.allposts.splice(idx, 1);
            }).then(function () {
                alert("Eliminacion satisfactoria");
            }).catch(function (errors) {
                console.log("Fallo por: " + errors);
            })
        }
    };
    $scope.showModal = function(post) {
        $scope.new_post = post;
        $('#modal_post').modal('show');
        console.log(post.id)
        console.log($scope.new_post);
    }
}]);
app.controller("PostCRUDController", ['$scope', 'Post', function($scope, Post) {


}]);
app.controller("CMisCanales", ['$scope', '$window', 'Canal', 'AreasResource', 'Post', function($scope, $window, Canal, AreasResource, Post) {
    $scope.canals = Canal.query();
    $scope.postsPorCanal = Post.query();
    $scope.nombre_boton = "Crear";
    //$scope.canales = CanalResource.query();
    $scope.canals.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
    $scope.id_can="";
    $scope.Redireccionar = function(dato){
        console.log(dato);
        $scope.canale = $scope.canals[dato-1];
        console.log($scope.canale);
        $window.location.href = "http://localhost:8000/red/canalprincipal?canal="+dato;
        $scope.id_can = dato;
    };

    var fecha_hoy = new Date();
    $scope.misareas = {
        model: [-1],
        opciones: AreasResource.query(),
        opcionSeleccionada:[-1]
    };

    //$scope.new_canal = new Canal();
    $scope.Guardar = function(new_canal, selectedareas) {
        //$scope.new_canal = new Canal({fecha_creacion: fecha_hoy.getFullYear()+"-"+fecha_hoy.getMonth()+"-"+fecha_hoy.getDate(), autor: 'user1', areas: areas_cono});
        if(!new_canal.pk){
            var nuevo_canal = new Canal();
            nuevo_canal.id = new_canal.id;
            nuevo_canal.nombre = new_canal.nombre;
            nuevo_canal.descripcion = new_canal.descripcion;
            nuevo_canal.fecha_creacion = fecha_hoy.getFullYear()+"-"+fecha_hoy.getMonth()+"-"+fecha_hoy.getDate();
            nuevo_canal.autor = $scope.usuario;
            nuevo_canal.areas = [];
            console.log(selectedareas);
            for (var i=0; i<selectedareas.length; i++){
                nuevo_canal.areas[i] = parseInt(selectedareas[i]);
            }
            nuevo_canal.$save(function () {
                $scope.canals.push(nuevo_canal);
            }).then(function () {
                $scope.new_canal = new Canal();
                $('#modal_canal').modal('hide');
                $scope.Reset();
            }).catch(function (errors) {
                $scope.errors = null
                console.log(errors);
            });
        }else{
            alert("El id ya existe!");
            new_canal.$update();
        }
    };
    $scope.remove = function(canal) {
        canal.$remove(function() {
            var idx = $scope.canals.indexOf(canal);
            $scope.canals.splice(idx, 1);
        }).then(function() {
            alert("Eliminacion satisfactoria");
            $scope.Reset();
        }).catch(function(errors) {
            console.log("Fallo por: "+errors);
        })
    };

    $scope.showModal = function(new_canal) {
        $scope.new_canal = new_canal;
        $scope.nombre_boton = "Actualizar";
        $('#modal_canal').modal('show');
        
    }

    $scope.Reset=function() {
        $scope.nombre_boton = "Crear";
        $scope.new_canal = new  Canal();
    }

}]);
app.controller("CCanal", ['$scope', '$routeParams', '$location','Canal',function($scope, $routeParams, $location, Canal) {

    $scope.misparams = function(){
        var url= location.search.replace("?", "");
        var arrUrl = url.split("&");
        var urlObj={};
        for(var i=0; i<arrUrl.length; i++){
            var x= arrUrl[i].split("=");
            urlObj[x[0]]=x[1]
        }
        return urlObj;
    };
    console.log($routeParams.canal);
    console.log($scope.misparams().canal);
    $scope.allcanals = Canal.get({pk: $scope.misparams().canal });
}]);
app.controller("CComentariosPorPost", ['$scope', 'ComentariosPorPostResource', function($scope, $routeParams, ComentariosPorPostResource) {
    $scope.comentarios = ComentariosPorPostResource.query();
    $scope.comentarios.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });

}]);
app.controller("Bichito",['$scope', 'ConfigResource', function($scope, ConfigResource, $resource) {
    nEditar = {};
   $scope.posts = [];
   $scope.newPost = {};
    $scope.usuarios = ConfigResource.query();
    $scope.usuarios.$promise.then(function(data) {
        console.log(JSON.stringify(data));
       $scope.posts = data;
    })
    $scope.posts = Post.query();
   /* $scope.addPost = function () {
        $scope.post("http://127.0.0.1:8000/red/api_users",{
            nombres: $scope.newPost.nombres,
            username: $scope.newPost.username,
            email: $scope.newPost.email,
            password: $scope.newPost.password,
            telefono_movil: $scope.newPost.telefono_movil
        })
            .success(function (data,status,headers, config) {
                $scope.posts.push($scope.newPost);
                $scope.addPost = {};
            })
            .error(function (error, status, headers, config) {
                console.log(error)

            })

    }
        
*/


}]);
app.controller("AreasConocimiento", ['$scope', 'AreasResource', function($scope, AreasResource) {
    $scope.areas = AreasResource.query();
    $scope.areas.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
}]);

app.controller("Seguido",['$scope', 'SeguidResource', function($scope, SeguidResource) {
 $scope.seguidor = SeguidResource.query();
    $scope.seguidor.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
}]);

app.controller("listpost",['$scope', 'listapostResource', function($scope, listapostResource) {
 $scope.lpost = listapostResource.query();
    $scope.lpost.$promise.then(function(data) {
        console.log(JSON.stringify(data));
    });
}]);