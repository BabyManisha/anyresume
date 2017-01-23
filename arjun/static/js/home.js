// Our Custom JS
$(document).ready(function () {
  //your code here

  	Vue.component('home', {
  	    template: "#app-home",
  	    data: function(){
  	    	return {
  	    		activeApp: this.$parent.activeApp,
  	    		details: {},
            name: Arjun.name,
            qualification: Arjun.qualification,
            phone: Arjun.phone,
            email: Arjun.email,
            location: Arjun.location,
            info: Arjun.info,
            info1: Arjun.info1
  	    	}
  	    }
  	});


    Vue.component('education', {
        template: "#app-education",
        data: function(){
          return {
            activeApp: this.$parent.activeApp,
            educationDetails: {},
          }
        },
        created (){
          var self = this;
          var url = "/arjun/educationPage";
          $.get(url, function( data ) {
            self.educationDetails = JSON.parse(data);
          });
        }
    });

    Vue.component('experience', {
        template: "#app-experience",
        data: function(){
          return {
            activeApp: this.$parent.activeApp,
            experienceDetails: {},
            roleKeys: []
          }
        },
        created (){
          var self = this;
          var url = "/arjun/experiencePage";
          $.get(url, function( data ) {
            self.experienceDetails = JSON.parse(data);
            for(let e in self.experienceDetails){
              let edata = self.experienceDetails[e];
              self.roleKeys.push(Object.keys(edata['roleName']));
            }
          });
        }
    });

    Vue.component('about', {
        template: "#app-about",
        data: function(){
          return {
            activeApp: this.$parent.activeApp,
            aboutDetails: {},
          }
        },
        created (){
          var self = this;
          var url = "/arjun/aboutPage";
          $.get(url, function( data ) {
            self.aboutDetails = JSON.parse(data);
          });
        }
    });

    Vue.component('contact', {
        template: "#app-contact",
        data: function(){
          return {
            activeApp: this.$parent.activeApp,
            firstName: "",
            lastName: "",
            email: "",
            mobile: "",
            message: "",
            msg: mesg
          }
        },
        methods: {
          sendMail () {
            var self = this;
            // if(self.firstName.length > 0 && self.lastName.length > 0 && 
              // self.email.length > 0 && self.mobile.length > 0 && self.message.length > 0){
              $.POST( 'contactMessage', { 
                'firstName' : firstName,
                'lastName' : lastName,
                'email' : email,
                'mobile' : mobile,
                'message' : message
              })
                .done(function( res ) {
                  console.log( "JSON Data: " + res );
                })
                .fail(function( jqxhr, textStatus, error ) {
                  var err = textStatus + ", " + error;
                  console.log( "Request Failed: " + err );
              });
            // }else{
            //   alert("PLease Provide Details..");
            // }
          }
        }
    });

    var App = new Vue({
    	el: '#app',
    	data: function () {
        	return {
            activeApp: 'Home',
            name: Arjun.name,
            qualification: Arjun.qualification,
            phone: Arjun.phone,
            email: Arjun.email,
            location: Arjun.location,
            info: Arjun.info,
            info1: Arjun.info1
        	}
    	},
      methods: {
        changeApp (app) {
          this.activeApp = app;
        }
      }
    })

});