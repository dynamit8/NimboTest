module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    svgstore: {
    options: {
      prefix : 'icon-', // This will prefix each ID
      svg: { // will add and overide the the default xmlns="http://www.w3.org/2000/svg" attribute to the resulting SVG
        viewBox : '0 0 100 100',
        xmlns: 'http://www.w3.org/2000/svg',
        style: 'display:none;',
      }
    },
    files: {
      'all.svg': ['*.svg'],
    },
  },
    pkg: grunt.file.readJSON('package.json'),
  });
  grunt.loadNpmTasks('grunt-svgstore');


  // Default task(s).
  grunt.registerTask('default', ['svgstore']);
  
};