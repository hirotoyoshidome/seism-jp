// #include <mapnik/map.hpp>
// #include <mapnik/load_map.hpp>
// #include <mapnik/agg_renderer.hpp>
// #include <mapnik/image.hpp>
// #include <mapnik/image_util.hpp>

// int main()
// {
//     mapnik::Map m(256,256);
//     mapnik::load_map(m, "./file.xml");
//     m.zoom_all();
//     mapnik::image_rgba8 im(256,256);
//     mapnik::agg_renderer<mapnik::image_rgba8> ren(m, im);
//     ren.apply();
//     mapnik::save_to_file(im, "the_image.png");

//     return 0;
// }
