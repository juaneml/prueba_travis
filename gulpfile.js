guplp.task('coveralls',['test'],function(){ gulp.src('coverage/lcov.info').pipe(coveralls());})
guplp.task('coveralls',['test'],function(){
    console.log('Prueba travis')
})