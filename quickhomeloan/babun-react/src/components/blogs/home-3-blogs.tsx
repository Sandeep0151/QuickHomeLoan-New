import { NavLink } from 'react-router-dom';
// internal
import BlogItemThree from "./blog-item/blog-item-three";
import blog_data from '../../data/blog-data';

const HomeThreeBlogs = () => {
  const blog_item = blog_data.filter((b) => b.page === "home");
  return (
    <div className="blog-section-three position-relative mt-160 lg-mt-80 mb-150 lg-mb-80">
      <div className="container">
        <div className="position-relative">
          <div className="title-one mb-20 lg-mb-10">
            <h2 className="text-dark">Latest News.</h2>
          </div>
          <p className="text-lg mb-30 lg-mb-10">
            Get the latest update, trips & tricks from our expert.
          </p>

          <div className="row gx-xl-5">
            {blog_item.map((b, i) => (
              <div key={i} className="col-md-6">
                <BlogItemThree blog={b} />
              </div>
            ))}
          </div>

          <div className="section-btn md-mt-50">
            <NavLink to="/blog" className="btn-eleven d-inline-flex align-items-center">
              <span className="text">See all blogs</span>
              <div className="icon tran3s rounded-circle d-flex align-items-center">
                <img
                  src="static/assets/images/icon/icon_27.svg"
                  alt="icon"
                  className="lazy-img"
                />
              </div>
            </NavLink>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomeThreeBlogs;
