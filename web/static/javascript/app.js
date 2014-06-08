(function (requirejs) {

  'use strict';

  requirejs.config({
    baseUrl: '../static/javascript',
    paths: {
      // libs
      soma: '../javascript/vendor/soma/soma-v2.0.4.min',
      template: '../javascript/vendor/soma-template/soma-template-v0.2.1.min',
      director: '../javascript/vendor/director/director.min',
      jquery: '//cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min',
    },
    shim: {
      'template': {
        deps: ['soma']
      },
    }
  });

  requirejs([
    'soma',
    'template',
    'jquery',
    'director',
  ], function (soma
                , template
                , jQuery
                ) {

    var Navigation = function(router, dispatcher) {

      var prefix = 'view-';
      var currentView = 'home';

      //router.init('/app');
      router.init();

      router.on('/.*/', function() {
        dispatchRoute(router.getRoute()[0]);
      });

      function dispatchRoute(viewId) {
        if(currentView != viewId) {
          $('#' + prefix + currentView).toggleClass('view-show view-hide');
          $('#' + prefix + viewId).toggleClass('view-show view-hide');
          currentView = viewId;
        }
      }

    };

    var InlocoApp = soma.Application.extend({
      init: function () {
        console.log('Start app.init');
        this.injector.mapValue('router', new Router());
        console.log('End app.init');
      },

      start: function () {
        console.log('Start app.start');
        this.injector.createInstance(Navigation);
        console.log('End app.start');
      }
    });

    // create the application
    new InlocoApp();

  });


})(requirejs);