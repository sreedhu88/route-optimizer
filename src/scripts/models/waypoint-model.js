module.exports = Backbone.Model.extend({
    defaults: {
        latitude: '',
        longitude: '',
        name: '',
        selected: false
    },

    getLatLong: function() {
        var myLatlng = new google.maps.LatLng(this.get('latitude'), this.get('longitude'));
        return myLatlng;
    }

});
