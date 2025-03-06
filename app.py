from flask import Flask, render_template_string,request,render_template,send_file
from eng import eng_page
from arb import arb_page
import pandas as pd

app = Flask(__name__)
def excel_to_dict_array(file,sheet_name):
    df = pd.read_excel(file,sheet_name=sheet_name)
    return df



@app.route('/',methods=['GET', 'POST'])
def generate_html():
    # Meta data 
    # Upload the excel file

    if request.method == "POST":
      lang = request.form['language']
      if 'file' not in request.files:
          return 'No file part'
      file = request.files['file']
      if file.filename == '':
          return 'No selected file'
      if file:
          dict_array = excel_to_dict_array(file,"Main Data")
      
      # Read that file
      # Generate the html file to upload on aem

      content_start_point = []
    

      for index, row in dict_array.iterrows():
          # Convert each row to a dictionary and append to the list
          # Convert one by one each row to a dict and adding to the list in the end 
          
          content_start_point.append(row.to_dict())

      # -------------------------------------------------------

      meta_data = {}


      for n in content_start_point:
            if n['content'] == 'total_tags':
                meta_data[n['content']]= int(n['data']) 
            elif n['content'] == 'total_products':
                meta_data[n['content']]= int(n['data']) 
            elif n['content'] == 'total_faqs':
                meta_data[n['content']]= int(n['data']) 
            else:       
                meta_data[n['content']] = n['data']

      # Content part
      content_start_point = []
      
      if file:
          dict_array = excel_to_dict_array(file,"Content")

      # print(dict_array)
      for index, row in dict_array.iterrows():
          # Convert each row to a dictionary and append to the list
          content_start_point.append(row.to_dict())
      content_data = ""
      swiper_id = 0
      review_images = 0 # to keep continuing review images until its 0 again
      previous_review = False
      newReview = True
      review_content_section=False
      review_show_content = ""
      review_hide_content = ""
      images_div = ""
      for n in content_start_point:
          if review_images == 0 and n["content"] != "review_show" and n["content"] != "review_hide":
            if n["content"] == "h1_p":
                content_data += f"""
                <div class="editable-content" style="margin-top: 10px">
                  <p dir="ltr">
                    { n["data"] }
                  </p>
                </div>
                """

            elif n["content"] == "h2":
                content_data += f"""
                <div
                  class="editable-content d-flex"
                  style="margin-top: 20px !important"
                >
                  <div
                    class="editable-content-bullet"
                    style="margin-left: 0px !important"
                  >
                    <h2
                      dir="ltr"
                      style="font-family: Roboto, sans-serif !important"
                    >
                      {n['data']}
                    </h2>
                  </div>
                </div>
                """

            elif n["content"] == "h2_p":
                content_data += f"""
                <div class="editable-content d-flex">
                  <div class="editable-content-number-1 bullet-point">
                    <p dir="ltr"></p>
                  </div>
                  <div class="editable-content-bullet">
                    <p dir="ltr">
                      {n['data']}
                    </p>
                  </div>
                </div>


                """

            elif n["content"] == "h3":
                content_data += f"""
                <div class="editable-content d-flex">
                  <div class="editable-content-bullet bullet-point">
                    <p
                      dir="ltr"
                      class="bullet-heading-gap"
                      style="margin-bottom: 0"
                    ></p>
                  </div>
                  <div class="editable-content-bullet-heading">
                    <h3
                      dir="ltr"
                      class="bullet-heading-gap"
                      style="font-family: Roboto, sans-serif !important"
                    >
                    {n['data']}
                    </h3>
                  </div>
                </div>    
            
                """

            elif n["content"] == "h3_p":
                content_data += f"""
                <div class="editable-content d-flex">
                  <div class="editable-content-number-1 bullet-point">
                    <p dir="ltr"></p>
                  </div>
                  <div class="editable-content-bullet">
                    <p dir="ltr">
                      {n['data']}
                    </p>
                  </div>
                </div>
                """

            elif n["content"] == "img":
                content_data += f"""
                <div class="image-wrapper mb-4">
                    <canvas
                      class="image-placeholder"
                      height="5"
                      width="8"
                    ></canvas>
                    <img
                      class="js-lazy-image lazy"
                      src="{n['data']}"
                      alt="{n['alt']}"
                    />
                </div>
                """
            elif n["content"] == "h4":
                content_data += f"""
                <div class="editable-content d-flex">
                    <div class="editable-content d-flex">
                        
                            <div class="editable-content-bullet" style="margin-left:0px !important">
                                <h4 dir="ltr" style="font-family: Roboto,sans-serif  !important;">
                                    {n['data']}
                                </h4>
                            </div>
                    </div>
                </div>
                """

            elif n["content"] == "h4_p":
                content_data += f"""
                <div class="editable-content d-flex">
                  <div class="editable-content d-flex">
                          <div class="editable-content-number-1 bullet-point">
                              <p dir="ltr"></p>
                          </div>	
                          <div class="editable-content-bullet">
                              <p dir="ltr">
                              {n['data']}
                              </p>
                          </div>
                  </div>
                </div>
                """

            elif n["content"] == "review_number":
                
                if previous_review == True:
                  # Close the previous review if new review just started
                  content_data = content_data.replace(f"""{swiper_id}reviewhidecontent""", review_hide_content)
                  review_hide_content = ""
                  scriptcontent = """
                  var swiper"""+str(swiper_id)+""" = new Swiper("#slider_"""+str(swiper_id)+"""", {
                      effect: "coverflow",
                      grabCursor: true,
                      centeredSlides: true,
                      loop: true,
                      coverflowEffect: {
                        rotate: 0,
                        stretch: 50,
                        depth: 200,
                        modifier: 2,
                        slideShadows: true,
                      },
                      loop: true,
                      // Navigation arrows
                      pagination: {
                        //pagination(dots)
                        el: "#slider-pagination-"""+str(swiper_id)+"""",
                      },
                      navigation: {
                        nextEl: "#slider-next-"""+str(swiper_id)+"""",
                        prevEl: "#slider-prev-"""+str(swiper_id)+"""",
                      },
                      keyboard: {
                        enabled: true,
                      },
                      mousewheel: {
                        thresholdDelta: 70,
                      },
                      breakpoints: {
                        560: {
                          slidesPerView: 1.5,
                        },
                        768: {
                          slidesPerView: 2,
                        },
                        1024: {
                          slidesPerView: 2,
                        },
                      },
                    });
                  """
                  content_data = content_data.replace(f"""scriptcontent""", scriptcontent)
                  scriptcontent = ""
                  # -------------------- till here ----------------------
                  previous_review = False

                swiper_id = n["data"]

            
            
            elif n["content"] == "review_title":
                ## Review title - done
                content_data += f"""
                  <div class="ml-3 mr-3 mx-sm-3 mx-md-5 mx-lg-5 mt-5">
                    <section class="m-0" id="{swiper_id}review_number">
                      <h2 style="font-size: 26px">"{swiper_id}headingcontent"</h2>
                      <div class="swiper-container">
                        <div class="swiper" id="slider_{swiper_id}">
                          <div class="swiper-wrapper">
                            {swiper_id}imagescontent
                          </div>
                        </div>
                        <div class="swiper-pagination" id="slider-pagination-{swiper_id}"></div>

                        <div class="swiper-button-prev" id="slider-prev-{swiper_id}">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            class="w-6 h-6"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M19.5 12h-15m0 0l6.75 6.75M4.5 12l6.75-6.75"
                            />
                          </svg>
                        </div>
                        <div class="swiper-button-next" id="slider-next-{swiper_id}">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke-width="1.5"
                            stroke="currentColor"
                            class="w-6 h-6"
                          >
                            <path
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              d="M4.5 12h15m0 0l-6.75-6.75M19.5 12l-6.75 6.75"
                            />
                          </svg>
                        </div>
                      </div>
                    </section>
                    <section class="my-5 custom-width">
                      <div class="row m-0">
                        <div class="col-auto text-left text-nowrap p-0">
                          <h3 class="text-dark">{swiper_id}customernamecontent</h3>
                        </div>
                        <div class="col review-section fs">
                          <div class="row">
                            <div
                              class="col-12 col-sm-auto col-lg-auto px-sm-1 px-lg-1"
                            >
                            {swiper_id}ratingcontent
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="row p-0 m-0">
                        <div class="col-12 p-0">
                          <div class="review-details m-0">
                            {swiper_id}reviewshowcontent
                          </div>
                        </div>
                        <div class="col-12 p-0 mt-2">
                          <div
                            class="review-details m-0"
                            id="show-content-{swiper_id}"
                            style="display: none"
                          >
                            {swiper_id}reviewhidecontent
                          </div>
                          <div class="row m-0 p-0">
                            <div
                              class="col-12 p-0"
                              style="display: flex; justify-content: start"
                            >
                              <button
                                id="view_more_btn-{swiper_id}"
                                class="btn d-flex btn-custom"
                                onclick="view_more('view_more_btn-{swiper_id}','show-content-{swiper_id}','view_less_btn-{swiper_id}')"
                              >
                                Read more &nbsp<i
                                  class="fa fa-angle-down fa-lg pt-2"
                                  aria-hidden="true"
                                ></i>
                              </button>
                            </div>
                            <div
                              class="col-12 p-0"
                              style="display: flex; justify-content: start"
                            >
                              <button
                                id="view_less_btn-{swiper_id}"
                                class="btn d-flex btn-custom"
                                onclick="view_less('view_more_btn-{swiper_id}','show-content-{swiper_id}','view_less_btn-{swiper_id}')"
                                style="visibility: hidden"
                              >
                                Collapse &nbsp<i
                                  class="fa fa-angle-up fa-lg pt-2"
                                  aria-hidden="true"
                                ></i>
                              </button>
                            </div>
                          </div>
                        </div>
                      </div>
                    </section>
                    
                  </div>
                  <script>scriptcontent</script>
                """
                heading_content = f'''{n["data"]}'''
                content_data = content_data.replace(f"""{swiper_id}headingcontent""", heading_content)
                pass
            
            elif "images_count" in n["content"]:
                # Total images are refreshed 
                review_images  = int(n["data"])
            elif n["content"] == "review_customer_name":
              ## Customer name will be here - done
              customernamecontent = f'''{n["data"]}'''
              content_data = content_data.replace(f'''{swiper_id}customernamecontent''', customernamecontent)
              
          
            elif n["content"] == "review_rating":
                ## Rating out of 5 stars - done
                total_stars = int(n["data"])
                reviewcontent = ""
                for i in range(1,6):
                  if total_stars>=i:
                    reviewcontent+='''
                      <i class="fa fa-star" style="color: #fcd53f" aria-hidden="true"></i>
                    '''
                  else:
                    reviewcontent+='''
                      <i class="fa fa-star" aria-hidden="true"></i>
                    '''

                reviewstars = f'''{reviewcontent}'''
                content_data = content_data.replace(f"""{swiper_id}ratingcontent""", reviewstars)
          else:
            if "r_image" == n["content"]:
                   
                images_div += f'''
                <div
                  class="swiper-slide swiper-slide--one"
                  style="
                    background-image: url({n["data"]});
                    background-position: left;
                  "
                >
                  <div class="slide-content"></div>
                </div>
                '''
                if review_images == 1:
                  content_data = content_data.replace(f"""{swiper_id}imagescontent""", images_div)
                review_images -= 1
                #Add that image
                
            elif n["content"] == "review_show":
              if n["type"] == 'h4':
                review_show_content += f'''
                  <div class="editable-content">
                    <h4>
                      {n["data"]}
                    </h4>
                  </div>
                '''
              elif n["type"] == "p":
                review_show_content+=f'''
                  <div class="editable-content">
                    <p>
                      {n["data"]}
                    </p>
                  </div>  
                '''
            elif n["content"] == "review_hide":
              previous_review = True
              if review_show_content != "":
                  content_data = content_data.replace(f"""{swiper_id}reviewshowcontent""", review_show_content)
                  review_show_content = ""
                 
              if n["type"] == 'h4':
                review_hide_content += f'''
                  <div class="editable-content">
                    <h4>
                      {n["data"]}
                    </h4>
                  </div>
                '''
              elif n["type"] == "p":
                review_hide_content += f'''
                  <div class="editable-content">
                    <p>
                      {n["data"]}
                    </p>
                  </div>  
                '''
      print(content_data)

      if lang == "english":
        new_data = eng_page.replace("<div>Contenthere</div>", content_data)
      elif lang == "arabic":  
        new_data = arb_page.replace("<div>Contenthere</div>", content_data)
      
      rendered_html = render_template_string(new_data,meta_data = meta_data)
      
    
      # Save the HTML to a file
      if lang == "english":
        with open("lg-story-en.jsp", "w",encoding="utf-8") as f:
            f.write(rendered_html)
        return send_file("lg-story-en.jsp", as_attachment=True)

      elif lang == "arabic":
        with open("lg-story-ar.jsp", "w", encoding="utf-8") as f:
            f.write(rendered_html)
        return send_file("lg-story-ar.jsp", as_attachment=True)

      ## Download the html file in return

      # return rendered_html
    else:
      return render_template("index.html")
     

if __name__ == '__main__':
    app.run(debug=True)