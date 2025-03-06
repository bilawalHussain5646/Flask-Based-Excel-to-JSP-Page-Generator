arb_page = """
<%@ page language="java" pageEncoding="UTF-8" contentType="text/html; charset=UTF-8"%>
<%@ include file="/WEB-INF/jsp/gp/common/include/head/head.jsp" %> 

<head>	

    <!-- chrome audits -->

 <!-- default code -->
 <%@ include file="/WEB-INF/jsp/gp/common/include/head/meta-default-tag.jsp" %>
 <!-- sns tag -->
 <%@ include file="/WEB-INF/jsp/gp/common/include/head/meta-sns-tag.jsp" %> 
	
<meta name="theme-color" content="#a50034"/>
<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
<link href="/ae_ar/lg-story/assets/styles/components/icons/css/font-awesome.min.css" rel="stylesheet" />
<link href="/ae_ar/lg-story/css/main.css" rel="stylesheet" />
<link href="/ae_ar/lg-story/assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
<link href="/ae_ar/lg-story/assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
<link href="/ae_ar/lg-story/assets/css/style.css" rel="stylesheet">
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css"
/>
<link rel="stylesheet" href="/ae/lg-story/scoop/lg-smart-dehumidifier-reviews-from-customers/style.css" />

<script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>


<base href="{{ meta_data['link'] }}">
<link rel="canonical" href="{{ meta_data['link'] }}" />

<!-- Add your title here -->
<title>{{ meta_data['title'] }}  </title>

<!-- Add your description here -->
<meta name="Description" content="{{ meta_data['description'] }}"/>



<!-- Add your keywords here -->
<!-- facebook / regular social metatags -->




<meta property="og:site_name" content="{{ meta_data['title'] }} " />

<!-- Add your Og details  -->
<meta property="og:title" content="{{ meta_data['title'] }} " />
<meta property="og:description" content="{{ meta_data['description'] }}" />
<meta property="og:url" content="{{ meta_data['link'] }}" />
<meta property="og:image" content="{{ meta_data['thumbnail_img_link'] }}" />
<meta itemprop="image" content="{{ meta_data['thumbnail_img_link'] }}" />
<!-- ------------------- -->

<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:site" content="@LG STORY"/>

<!--  Add your twitter details here  -->
<meta name="twitter:title" content="{{ meta_data['title'] }}  "/>
<meta name="twitter:description" content="{{ meta_data['description'] }}"/>
<meta name="twitter:image" content="{{ meta_data['thumbnail_img_link'] }}"/>
<!--Add additional meta properties-->


    <meta property="og:type" content="{{ meta_data['main_tag'] }}"/>
    <meta name="Subject" content="{{ meta_data['title'] }}  "/>


<!-- Dont change anything below  -->
<!-- your css-->
<style>
     @font-face {
  font-family: 'FontAwesome';
  src:  url('/ae_ar/lg-story/assets/styles/components/icons/fonts/fontawesome-webfont.eot?v=4.2.0');
  src:  url('/ae_ar/lg-story/assets/styles/components/icons/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), 
        url('/ae_ar/lg-story/assets/styles/components/icons/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), 
        url('/ae_ar/lg-story/assets/styles/components/icons/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'),
        url('/ae_ar/lg-story/assets/styles/components/icons/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.a_tag_inline{
    display:contents;
}
.bullet-point{
    padding-top:7px;
    white-space: nowrap;
}
@media screen and (max-width: 1024px) {
    .bullet-point{
        padding-top:2px;
    }  
}

h1, h2, h3, h4, h5, h6 {
    font-family: Roboto,sans-serif  !important;
    
}
h1{
    text-transform: none !important;
    font-weight: 700 !important;
}
h2{
    font-size:30px;
}
h3{
    font-size:32px;
    font-family: Roboto,sans-serif  !important;
    font-weight:700 !important;
}
.tags-custom{
    font-family: 'Open Sans' !important;
    font-size: 1.125rem !important;
    line-height: 1.4 !important;
    
    font-weight: bolder !important;
}
.editable-content{
    
    margin:0  !important;
}
.editable-content.d-flex{
    margin:0px 100px  !important;
}
.editable-content-bullet-description{
    margin:0px 60px  !important;
}
.editable-content-bullet{
    font-family: Roboto,sans-serif  !important;
    margin: 0px 10px !important;
}
.editable-content-bullet h3{
    font-family: Roboto,sans-serif  !important;
}
@media only screen and (max-width: 768px){
    .editable-content {
        margin: 20px 0px !important;
}
    .editable-content.d-flex{
        margin:0px !important;
    }
    .editable-content-bullet-description{
        margin:0px 0px  !important;
    }
}
p{
    font-family: 'Open Sans' !important;
   font-size: 1.125rem  !important;
    margin-top: 20px  !important;
    margin-bottom: 20px  !important;
    line-height: 1.6  !important; 
}
.promos-wrapper, .image-wrapper{
    border-radius: 15px !important;
}
.gt-wrapper .gt-content .sidebar .promos-wrapper{
    border:1px solid #c6c6c6 !important;
}
.entry-container .image-wrapper {
    border-radius: 15px 15px 0px 0px !important;
}
.entry-container .image-wrapper .inner {
    padding: 20px 20px 10px !important;
        margin: 0 !important;
        height:100% !important;
        width:100% !important;
}
.color-font{
    font-family: Roboto,sans-serif  !important;
}
.tags-list {
    font-family:'Open Sans' !important;
}
.gt-wrapper .inner {
    margin: 7.5px 0px !important;
    padding: 5px 0px !important;
}
.tooltip{
    padding-right:0px !important;
}
.gt-wrapper .page-details {
    margin-top: 15px;
    margin-bottom: 0px !important;

}
@media only screen and (min-width: 769px){
    .gt-wrapper .sidebar {
        padding-top: 12px;
    }
}

.gt-header img {
    padding: 20px 60px !important;
    width: 300px !important;
}
.date-custom{
    margin: 15px 0px !important;
}
.mainmenu a {
    font-size: 20px !important;
    line-height: 31px !important; 
    padding: 5px 15px !important;
    font-weight: 600 !important;
}
.mainmenu #mainmenu-flters li {
    padding: 0px !important;
    font-size: 14px;
    font-weight: 400;
    line-height: 1;
    text-transform: uppercase;
    margin-bottom: 5px;
    transition: all 0.3s ease-in-out;
    border-radius: 15px;
    text-decoration: none;
}
.promo-title-featured-product{
    /* font-weight: 700 !important; */
    font-family: 'Roboto' !important;
    padding:0px 20px !important;
}
.gt-wrapper .tags-list li {
    margin-left: 25px !important;
}
.gt-wrapper .entry-box .inner{
    padding: 20px 20px 10px !important;
    border: 0px !important;
}
.entry-box .copy{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
 
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    max-height:50px !important;
}
.inner p{
    margin-top:0px !important;
    line-height:1.6 !important;

}
.gt-wrapper .editable-content a{
    font-family:'Open Sans' !important;
}
.gt-wrapper.editable-content p strong{
    font-family:"Open Sans", sans-serif;
}
.editable-content-bullet-heading{
    font-family: Roboto,sans-serif  !important;
    margin: 0px 10px !important;
}

.editable-content-number{
    font-family: Roboto,sans-serif  !important;
    margin: 0px 13px !important;
}
.editable-content-number-1{
    font-family: Roboto,sans-serif  !important;
    margin: 0px 19px !important;
}
.bullet-heading-gap{
    margin-bottom:5px !important
}
@media only screen and (max-width: 1024px){
    .editable-content-number {
        margin: 0px 7px !important;
    }
    .editable-content-number-1 {
        margin: 0px 12px !important;
    }
    .editable-content-bullet-heading {
        margin: 0px 7px !important;
    }
}
b{
    font-weight:900 !important;
}
table {
  
  border-collapse: collapse !important;
  width: 100% !important;
}

td, th {
  border: 1px solid #dddddd !important;
  text-align: center !important;
  padding: 8px !important;
}
</style>
<!-- custom branch styles -->
<style>
      .faq_section {
        /* font-family: "LG Smart", "Segoe UI", "Microsoft Sans Serif", sans-serif; */
        color: black;
      }
      .faq_heading {
        font-size: 60px;
        line-height: 60px;
        font-weight: 400;
        margin: 20px 0 0 0;
      }
      .question_heading {
        
        font-size: 18px !important;
        font-family:'Open Sans' !important;
      }
      .custom-transition {
        transition: 0.4s ease;
        cursor: pointer;
        -webkit-user-select: none; /* Safari */
        -ms-user-select: none; /* IE 10 and IE 11 */
        user-select: none; /* Standard syntax */
      }
      .answer {
        max-height: 0;
        overflow: hidden;
        opacity: 0;
        font-size:18px;
        font-family:'Open Sans' !important;
        transition: max-height 0.4s ease, opacity 0.4s ease;
      }
      .answer.show {
        max-height: 500px; /* Adjust based on content height */
        opacity: 1;
      }
</style>
<style>
      .fs {
        font-size: 1.5em;
        align-items: center;
        padding-left: 24px;
      }
      @media (max-width: 576px) {
        .fs {
          padding-top: 2px;
          font-size: 1.1em;
          padding-left: 14px;
        }
      }
      .profile-logo {
        padding: 20px 30px;
        font-size: 22px;
        border: 1px solid #faebd7;
        border-radius: 50px;
        background-color: #faebd7;
      }
      .review-section {
      }
      .search-tag {
        padding: 5px 10px;
        background-color: rgb(212, 239, 239);
        border-radius: 5px;
      }
      .review-details {
        text-align: justify !important;
      }
      .custom-width {
        width: 70%;
        margin: 0 auto !important;
      }
      @media (max-width: 575px) {
        .custom-width {
          width: 100%;
        }
      }
      .btn-custom{
        background-color:#efefef !important;
      }
       .swiper-container {
        margin: 0 auto;
        width: 100%;
      }
      @media (min-width: 760px) {
        .swiper-container {
          width: 100%;
        }
      }
      @media (min-width: 1024px) {
        .swiper-container {
          width: 850px;
        }
      }
    </style>
<!-- / custom branch styles -->
<script src="https://kit.fontawesome.com/27e8524286.js" crossorigin="anonymous"></script>
<script src="https://www.googleoptimize.com/optimize.js?id=OPT-5MNNSM7"></script>



<!-- Update According to your need (ASK FRANK) -->
<script type="application/ld+json">
{
  "@context": "http://schema.org",
  "@type": "Article",
  "mainEntityOfPage": "{{ meta_data['link'] }}/",
  "headline": "{{ meta_data['title'] }} ",
  "alternativeHeadline": "{{ meta_data['title'] }} ",
  "image": "{{ meta_data['thumbnail_img_link'] }}",
  "author": "",
  "genre": "{{ meta_data['sub_category'] }}",
  "keywords": "",
  "publisher": {
    "@type": "Organization",
    "name": "",
    "logo": {
      "type": "imageObject",
      "url": "https://www.lg.com/lg4-common-gp/img/global/header-large-logo.png"
    }
  },
  "url": "{{ meta_data['link'] }}",
  "dateCreated": "2024-03-23",
  "dateModified": "2024-03-23",
  "datePublished": "2024-03-23",
  "description": "{{ meta_data['description'] }} ",
  "articleBody": "{{ meta_data['description'] }} "
};
</script>

 
<!-- ------------------------------ -->
<!-- Do not update -->
                                                                                                    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600&amp;subset=cyrillic,cyrillic-ext,greek,greek-ext,latin-ext,vietnamese" rel="stylesheet">
                                                                                                    <link href="https://fonts.googleapis.com/css?family=Open+Sans+Condensed:700&amp;subset=cyrillic,cyrillic-ext,greek,greek-ext,latin-ext,vietnamese" rel="stylesheet">
                                                                                                    <link href="https://fonts.googleapis.com/css?family=Roboto+Slab&amp;subset=cyrillic,cyrillic-ext,greek,greek-ext,latin-ext,vietnamese" rel="stylesheet">


                                                                                                    <jsp:include page="/WEB-INF/jsp/gp/common/include/head/head-css.jsp" />
                                                                                                    <jsp:include page="/WEB-INF/jsp/gp/common/include/head/font-woff.jsp" />
                                                                                                    <jsp:include page="/WEB-INF/jsp/gp/common/include/head/mic-head-script.jsp" />
                                                                                                    <jsp:include page="/WEB-INF/jsp/gp/common/include/head/gateway-foresee.jsp" /> 

                                                                                                    </head>
                                                                                                    
                                                                                                    <body>



                                                                                                        <jsp:include page="/WEB-INF/jsp/gp/common/include/body/body-noscript.jsp" />
                                                                                                            <jsp:include page="/WEB-INF/jsp/gp/common/include/body/google-tag-manager.jsp" />
                                                                                                            <jsp:include page="/WEB-INF/jsp/gp/common/include/body/broswe-check-popup-layer.jsp" />  

                                                                                                    <div class="sr-only" itemscope itemtype="http://schema.org/WebPage">
                                                                                                            
                                                                                                    <meta itemprop="name" content="{Browser Title}"/>
                                                                                                            
                                                                                                    <meta itemprop="image" content="{Share Image}" />
                                                                                                            
                                                                                                    <meta itemprop="url" content="{Cannonical URL}" />
                                                                                                            
                                                                                                    <meta itemprop="description" content="{Page Description}" />
                                                                                                            
                                                                                                    <meta itemprop="Keywords" content="{Page Keyword}" />
                                                                                                        

                                                                                                    </div>
                                                                                                        
                                                                                                        

                                                                                                    <c:set var='bizType' value='${$bizType }' />
                                                                                                        
                                                                                                    <c:set var='siteType' value='MKT' />

                                                                                                        
                                                                                                    <!-- component (navigation) -->
                                                                                                        
                                                                                                    <c:import url="/${localeCd }/gnb">
                                                                                                            
                                                                                                    <c:param name="bizType" value="${bizType}"/>
                                                                                                            
                                                                                                    <c:param name="siteType" value="${siteType}"/>
                                                                                                            
                                                                                                    <c:param name="isMobile" value="${isMobile}"/>
                                                                                                        
                                                                                                    </c:import>
                                                                                                        

                                                                                                    <!-- top button -->
                                                                                                    <jsp:include page="/WEB-INF/jsp/gp/common/include/body/top.jsp" /> 
                                                                                                    <!-- // top button -->	


                                                                                                    <div id="content">	  	  
                                                                                                        <div id="content">
                                                                                                            <div class="gt-wrapper">
                                                                                                                <div class="gt-header">
                                                                                                                    <div class="container">
                                                                                                                        <a href="/ae_ar/lg-story/"><img src="/ae_ar/lg-story/images/LG-Story-logo.png"></a>
                                                                                                                                <section id="mainmenu" class="mainmenu">       
                                                                                                                                  <div class="row">
                                                                                                                                      <div class="col-lg-12 d-flex justify-content-center">
                                                                                                                                          <ul id="mainmenu-flters">
                                                                                                                                              <li><a  href="/ae_ar/lg-story/up-and-coming/" class="js-box-link" data-link-name="landing_thumbnail-lg-story/up-and-coming/">اكتشف المزيد</a></li>
                                                                                                                                              <li> <a href="/ae_ar/lg-story/helpful-guide" class="js-box-link" data-link-name="landing_thumbnail-lg-story/helpful-guide">تعلم واستفد</a></li>
                                                                                                                                              <li><a href="/ae_ar/lg-story/news/" class="js-box-link" data-link-name="landing_thumbnail-lg-story/news/">اخبار</a></li>
                                                                                                                                              <li><a href="/ae_ar/lg-story/scoop/" class="js-box-link" data-link-name="landing_thumbnail-lg-story/scoop/">مواضيع تهمك</a></li>
                                                                                                                                              <li><a href="/ae_ar/lg-story/lifes-good-people/" class="js-box-link" data-link-name="landing_thumbnail-lg-story/life-is-good/">شخصيات الحياة أجمل</a></li>
                                                                                                                                                      
                                                                                                                                          </ul> 
                                                                                                                                      </div>
                                                                                                                              
                                                                                                                                
                                                                                                                                  </div>
                                                                                                                                </section>
                                                                                                                      </div>
                                                                                                                </div>
                                                                                                                   
                                                                                                                    <div class="gt-content"> 
                                                                                                                        <div class="progress" style="--scroll:0%;"></div>
                                                                                                                        <div class="box-container maxW mb40">
                                                                                                                         <div class="page-header">
                                                                                                                        <div class="clearfix"></div>
                                                                                                                            <div class="inner">





                                                                                                                            <!-- Your title -->
                                                                                                                                <h1 class="page-title">{{ meta_data['h1'] }}  </h1>
                                                                                                                                <!--  -->

                                                                                                                                                                                                                                                        <div class="breadcrumb-article">
                                                                                                                                <!-- Your tags -->
                                                                                                                                <div class="breadcrumb-article">
                                                                                                                                    <ul class="list-inline tags-list ">
                                                                                                                                          <li>
                                                                                                                                            <a class="tags-custom" href="{{meta_data['main_tag_link'] }}">
                                                                                                                                              <b>{{ meta_data['main_tag'] }}</b>
                                                                                                                                            </a>
                                                                                                                                          </li>
                                                                                                                                          {% for n in range(1,meta_data['total_tags']+1) %}
                                                                                                                                          <li>
                                                                                                                                            <a
                                                                                                                                              class="tags-custom"
                                                                                                                                              href="{{ meta_data['tag_'+n|string+ '_link'] }}"
                                                                                                                                              ><b>{{ meta_data['tag_'+n|string] }}</b></a
                                                                                                                                            >
                                                                                                                                          </li>
                                                                                                                                          {% endfor %}
                                                                                                                                    <!--  -->
                                                                                                                                    </ul>
                            
                                                                                                                                </div>
                                                                                                                            <div class="page-details">
                                                                                                                                <div class="share-container">   
                                                                                                                                    <!-- Facebook Link -->

                                                                                                                                    <a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u={{ meta_data['link'] }}" data-link-name="social_share-facebook-{{ meta_data['link'] }}">
                                                                                                                                        <img src="/ae_ar/lg-story/assets/images/social-sharing/new_social_button-facebook.png"  style="max-width: 30px;" alt="Facebook" />
                                                                                                                                    </a> 

                                                                                                                                    <!-- Twitter Link -->
                                                                                                                                    <a target="_blank" href="https://twitter.com/intent/tweet?text={{ meta_data['title'] }}  &url={{ meta_data['link'] }}" data-link-name="social_share-twitter-{{ meta_data['link'] }}">
                                                                                                                                        <img src="/ae_ar/lg-story/assets/images/social-sharing/new_social_button-twitter.png" style="max-width: 30px;" alt="Twitter" />
                                                                                                                                    </a>

                                                                                                                                    <!-- Linkedin Link -->
                                                                                                                                    <a target="_blank" href="https://www.linkedin.com/shareArticle?mini=true&url={{ meta_data['link'] }}">
                                                                                                                                        <img src="/ae_ar/lg-story/assets/images/social-sharing/new_social_button-linkedin.png" style="max-width: 30px;" alt="linkedin" />
                                                                                                                                    </a>  

                                                                                                                                    <!--  -->
                                                                                                                                    <a class="mobile-displayed"  target="_blank" href="fb-messenger://share/?link={{ meta_data['link'] }}" data-link-name="social_share-facebook-messenger-{{ meta_data['link'] }}">
                                                                                                                                        <img src="/ae_ar/lg-story/assets/images/social-sharing/new_social_button_messenger.png" style="max-width: 30px;" alt="FacebookMessenger" />
                                                                                                                                    </a>
                                                                                                                                    <a class="mobile-displayed"  target="_blank" href="whatsapp://send?text=Check this out: {{ meta_data['link'] }}" data-link-name="social_share-whatsapp-{{ meta_data['link'] }}">
                                                                                                                                        <img src="/ae_ar/lg-story/assets/images/social-sharing/new_social_button_whatsapp.png" style="max-width: 30px;" alt="Whatsapp" />
                                                                                                                                    </a>
                                                                                                                                    <div class="tooltip">
                                                                                                                                        <button class="share__copy-link" onclick="myFunction()" href="javascript:void(0);" data-link-name="social_share-facebook-{{ meta_data['link'] }}/" style="background-color:transparent;" >
                                                                                                                                    
                                                                                                                                        <img src="/ae_ar/lg-story/assets/images/social-sharing/new_social_button-sharing.png"  style="max-width: 30px;" alt="share link"/>
                                                                                                                                        <span class="tooltiptext">Copy the link</span>
                                                                                                                                    <p id="linkcopied" class="tooltiptext"></p>
                                                                                                                                    </button> 
                                                                                                                                </div>
               
                                                                                                                            </div>

                                                                                                                            <p class="details"> 
                                                                                                                        
                                                                                                                        {{ meta_data['blog_date'] }}</p>
                                                                                                                           <div class="clearfix"></div>
                                                                                                                            </div>
                                                                                                                            <%-- Until date --%>

                                                                                                                                    
                                                                                                                                    
                                                                                                                                <div class="clearfix"></div>
                                                                                                                                
                                                                                                                        </div>
                                                                                                                    </div>
                                                                                                                    <div class="main-content box-8 box-tablet-8">           
                                                                                                                            

                                                                                                                


            <div class="module-editable-content">
                    <div class="inner">

                      <div>Contenthere</div>  
                      
                        
                        {% if meta_data['total_faqs'] %}
                        <div class="editable-content">
                            <section class="faq container">
                                <div class="faq_section">
                                    <h2 class="text-center faq_heading">FAQ</h2>

                                    {% for n in range(1,meta_data['total_faqs']+1) %}
                                                                            
                                    <div
                                    class="row m-0 mt-3 border border-1 p-3 px-4 custom-transition"
                                    onclick="toggleDiv('{{ 'faq_q'+n|string }}', '{{ 'faq_a'+n|string }}')"
                                    >
                                        <div class="col-auto text-right p-0" style="font-size:18px; font-family:'Open Sans'; margin-top:5px;">
                                            <i class="fa fa-plus" id="{{ 'faq_q'+n|string }}" aria-hidden="true"></i>
                                        </div>
                                        <div class="col">
                                            <div class="row">
                                                <div class="col-12">
                                                    <h3 data-role="trigger" tabindex="0">
                                                
                                                        {{ meta_data['faq_q'+n|string] }}
                                                
                                                    </h3>
                                                </div>
                                                <div class="col-12 answer" id="{{ 'faq_a'+n|string }}">
                                                    {{ meta_data['faq_a'+n|string] }}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    {% endfor %}
                                </div>
                            </section>
                        </div>
                        {% endif %}
                        <div class="editable-content">
                            <p dir="rtl"><strong style="font-family: Roboto,sans-serif  !important;">!Life's Good, LG</strong></p>
                        </div>

                    <div class="clearfix mb40"></div>
                


        

                    <!-- START READ MORE -->
                    <h3 style="text-align: center;">المزيد للقراءة</h3>
                  </div> 

                                                                                    

                                                                                    <div class="grid-container js-grid more-items-block" data-items="6">
                                                                                    <div class="box-container maxW mb40">
                                                                                    <div class="entry-box js-grid-item">



                                                                                                </div>
                                                                                                <div class="entry-box js-grid-item" style="height: 218px;">

                                                                                                    



                                                                                                
                                                                                                </div>
                                                                                                <div class="entry-box js-grid-item" style="height: 218px;">





                                                                                                </div>
                                                                                            <div class="entry-box js-grid-item">
                                                                                                


                                                                                                <div class="entry-container" style="border-radius: 15px !important; border: 1px solid #c6c6c6 !important; margin-left: 0px !important; margin-right:0px !important">
                                                                                                    <div class="image-wrapper">
                                                                                                    <canvas class="image-placeholder" height="5" width="8"></canvas>
                                                                                                    <a href="{{ meta_data['more_to_read_paragraph_1_link'] }}" class="js-box-link" data-link-name="landing_article-{{ meta_data['more_to_read_paragraph_1_link'] }}">
                                                                                                    <img class="js-lazy-image lazy" src="/ae/lg-story/assets/images/empty.png" data-src="{{ meta_data['more_to_read_image_1'] }}" alt="{{ meta_data['more_to_read_image_1_alt'] }}" style="display: block;" />
                                                                                                    </a>
                                                                                                    </div>
                                                                                                    <div class="copy-wrapper">
                                                                                                    <div class="inner">
                                                                                                    <p class="section  "><a class="uppercase blog color-red" href="{{ meta_data['cat_more_to_read_1_link'] }}" data-link-name="landing_category-{{ meta_data['cat_more_to_read_1_link'] }}">{{ meta_data['cat_more_to_read_1'] }}</a></p>
                                                                                                    <h3 class="entry-title">
                                                                                                    <a href="{{ meta_data['more_to_read_paragraph_1_link'] }}" class="color-font" data-link-name="landing_article-{{ meta_data['more_to_read_paragraph_1_link'] }}">{{ meta_data['more_to_read_heading_1'] }}
                                                                                                        </a>
                                                                                                    </h3>
                                                                                                    
                                                                                                    <p class="copy mb0 js-text-ellipsis"  style="line-height:1.3 !important;">{{ meta_data['more_to_read_paragraph_1'] }}
                                                                                                        
                                                                                                    
                                                                                                    </p>
                                                                                                    <a class="entry-link" href="{{ meta_data['more_to_read_paragraph_1_link'] }}" data-link-name="landing_article-{{ meta_data['more_to_read_paragraph_1_link'] }}">Learn more</a>
                                                                                                    </div>
                                                                                                    </div>
                                                                                                    </div> 

                                                                                    
                                                                                                


                                                                                            </div>
                                                                                        
                                                                                            <div class="entry-box js-grid-item">
                                                                                                <div class="entry-container" style="border-radius: 15px !important; border: 1px solid #c6c6c6 !important; margin-left: 0px !important; margin-right:0px !important">
                                                                                                    <div class="image-wrapper">
                                                                                                      <canvas class="image-placeholder" height="5" width="8"></canvas>
                                                                                                      <a href="{{ meta_data['more_to_read_paragraph_2_link'] }}" class="js-box-link" data-link-name="landing_article-{{ meta_data['more_to_read_paragraph_2_link'] }}">
                                                                                                      <img class="js-lazy-image lazy" src="/ae/lg-story/assets/images/empty.png" data-src="{{ meta_data['more_to_read_image_2'] }}" alt="{{ meta_data['more_to_read_image_2_alt'] }}" style="display: block; border-top-right-radius: 0px;"/>
                                                                                                      </a>
                                                                                                    </div>
                                                                                                    <div class="copy-wrapper">
                                                                                                      <div class="inner">
                                                                                                        <p class="section"><a class="uppercase blog color-red" href="{{ meta_data['cat_more_to_read_2_link'] }}" data-link-name="landing_category-{{ meta_data['cat_more_to_read_2_link'] }}">{{ meta_data['cat_more_to_read_2'] }}</a></p>
                                                                                                        <h3 class="entry-title">
                                                                                                        <a href="{{ meta_data['more_to_read_paragraph_2_link'] }}" class="color-font" data-link-name="landing_article-{{ meta_data['more_to_read_paragraph_2_link'] }}">{{ meta_data['more_to_read_heading_2'] }}
                                                                                                            </a>
                                                                                                        </h3>
                                                                                                        
        
                                                                                                        <p class="copy mb0 js-text-ellipsis" style="line-height:1.3 !important;">
                                                                                                            
                                                                                                        {{ meta_data['more_to_read_paragraph_2'] }}
                                                                                                        </p>
                                                                                                        <a class="entry-link" href="{{ meta_data['more_to_read_paragraph_2_link'] }}" data-link-name="landing_article-{{ meta_data['more_to_read_paragraph_2_link'] }}">Learn more</a>
                                                                                                      </div>
                                                                                                    </div>
                                                                                                </div>

                                                                                            </div>
                                                                                    </div>
                                                                                    <div class="clearfix mb40"></div>

                                                                                    </div>

                                                                                                                                                                                        </div>
                                                                                                                                                                                        
                                                                                                                                                                                    </div>
                                                                                                                                                                                    
                                                                                                                                                                                   
                                                                                                                                                                                    <div class="sidebar box-4 box-tablet-4">
                                                                                                                                                                                   
                                                                                                                                                                                            
                                                                                                                                                                                        

                                                                                                                            <div class="promos-wrapper" style="padding-bottom:20px !important">
				                                                                                                                        <h3 class="promos-wrapper-title ">المزيد للقراءة</h3>
                                                                                                                                {% for n in range(1,meta_data['total_products']+1) %}
                                                                                                                                  <div
                                                                                                                                    class="component-item impulse-promo impulse-promo"
                                                                                                                                    id="impulse-promo-613395e9ce834e3378933dc1"
                                                                                                                                  >
                                                                                                                                    <div class="promo">
                                                                                                                                      <div
                                                                                                                                        class="inner"
                                                                                                                                        style="padding: 0px 20px !important"
                                                                                                                                      >
                                                                                                                                        <div class="column-image">
                                                                                                                                          <div class="image-wrapper">
                                                                                                                                            <canvas
                                                                                                                                              class="image-placeholder"
                                                                                                                                              height="5"
                                                                                                                                              width="8"
                                                                                                                                            ></canvas>
                                                                                                                                            <a
                                                                                                                                              href="{{ meta_data['product_'+n|string+'_link'] }}"
                                                                                                                                              target="_blank"
                                                                                                                                              class="js-box-link"
                                                                                                                                            >
                                                                                                                                              <img
                                                                                                                                                class="js-lazy-image lazy"
                                                                                                                                                src="{{ meta_data['product_'+n|string+'_image'] }}"
                                                                                                                                                alt="{{ meta_data['product_'+n|string+'_title'] }}"
                                                                                                                                              />
                                                                                                                                            </a>
                                                                                                                                          </div>
                                                                                                                                        </div>
                                                                                                                                        <div class="column-text">
                                                                                                                                          <div class="copy-wrapper">
                                                                                                                                            <p class="section">
                                                                                                                                              <a
                                                                                                                                                class="color-red uppercase"
                                                                                                                                                href="{{ meta_data['product_'+n|string+'_link'] }}"
                                                                                                                                                >Events</a
                                                                                                                                              >
                                                                                                                                            </p>
                                                                                                                                            <p class="promo-title-featured-product">
                                                                                                                                              {{ meta_data['product_'+n|string+'_title'] }}
                                                                                                                                            </p>
                                                                                                                                            <p class="promo-copy-featured-product"></p>

                                                                                                                                            <div class="text-center mb10">
                                                                                                                                              <a
                                                                                                                                                class="btn-promo btn-outline btn-block"
                                                                                                                                                href="{{ meta_data['product_'+n|string+'_wtb_link'] }}"
                                                                                                                                                target='"_blank"'
                                                                                                                                                data-link-name="where_to_buy-GSXV91BSAE"
                                                                                                                                                >WHERE TO BUY
                                                                                                                                              </a>
                                                                                                                                            </div>
                                                                                                                                          </div>
                                                                                                                                        </div>
                                                                                                                                      </div>
                                                                                                                                    </div>
                                                                                                                                  </div>
                                                                                                                                {% endfor %}

                                                                                                                                

                                                                                                                                
                                                                                                                               
                                                                                                                                
                                                                                                                                
                                                                                                                            </div>	



                                                                                                                                </div>
                                                                                                                                <div class="clearfix"></div>
                                                                                                                            </div>

                                                                                                                            


                                                                                                                                </div>
                                                                                                                                <div class="clearfix"></div>
                                                                                                                            </div>
                                                                                                                        
                                                                                                                            </div>
                                                                                                                            </div>
                                                                                                                            </div>       
                                                                                                                        </div>







                                                                                                                            </div> 

                                                                                                                            </div>

                                                                                                                            <div class="module-editable-content-promo">
                                                                                                                                <div class="inner">


                                                                                                                                </div>
                                                                                                                            </div>




	


                                                                                                                                                    </script>
                                                                                                                                                    <script>
                                                                                                                                                        // When the user clicks on div, open the popup
                                                                                                                                                        function myFunction() {
                                                                                                                                                        var popup = document.getElementById("popupsocialicon");
                                                                                                                                                        popup.classList.toggle("show");
                                                                                                                                                        }
                                                                                                                                                        </script>
                                                                                                                                                    <!-- footer seo copy -->
                                                                                                                                                        
                                                                                                                                                    <c:import url="/${localeCd }/footerSeoCopy"/> 
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                    <c:import url="/${localeCd }/footer">
                                                                                                                                                            
                                                                                                                                                    <c:param name="bizType" value="${bizType}"/>
                                                                                                                                                            
                                                                                                                                                    <c:param name="siteType" value="${siteType}"/>
                                                                                                                                                        
                                                                                                                                                    </c:import>


                                                                                                                                                        <script>


        _dl = {
            page_name: {
                bu: "{{ meta_data['bu'] }}", // fixed value by LG Business Unit (ha, he, mc, xbu)
                super_category: "{{ meta_data['super_category'] }}",
                category: "lg-story",
                sub_category: "{{ meta_data['sub_category'] }}",
                page_purpose: "{{ meta_data['page_purpose'] }}", // Fixed value microsite
                product_year: "",
                model_id: "", // model, review page
                bundle_name: "", // bundle promotion
                promotion_name: "", // promotion detail page
                microsite_name: "{{ meta_data['microsite_name'] }}",
            }
                ,
            "country_code": "ae",
            "language_code": "ar",
            "page_category_l1": "ae:ha",
            "page_category_l2": "",
            "page_category_l3": "",
            "page_category_l4": "",
            "promotion_name": "",
            "products": "",
            "page_event": ""

        };


        // gtm
        var standardData = {};
        standardData = {
            "siteType": "B2C",
            "pageType": "home",
            "pdpStatus": "",
            "level1": "",
            "level2": "",
            "level3": ""
        };


        var dataLayer = window.dataLayer || [];
        dataLayer.push({
            '	event': 'dataLayer',
            'dataLayer': _dl,
            'standardData': standardData
        });
        function toggleDiv(faq_id, answer_id) {
        var sym = document.getElementById(faq_id);
        var ans = document.getElementById(answer_id);

        // Toggle the answer visibility
        ans.classList.toggle("show");

        // Toggle the icon
        if (sym.classList.contains("fa-plus")) {
          sym.classList.remove("fa-plus");
          sym.classList.add("fa-minus");
        } else {
          sym.classList.remove("fa-minus");
          sym.classList.add("fa-plus");
        }
      }

                                                                                                                                                                            </script>
                                                                                                                                                                        <!-- Vendor JS Files -->
                                                                                                                                                                        <script src="/ae/lg-story/assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
                                                                                                                                                                        <script src="/ae/lg-story/assets/vendor/glightbox/js/glightbox.min.js"></script>
                                                                                                                                                                        <script src="/ae/lg-story/assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
                                                                                                                                                                        <!-- Template Main JS File -->
                                                                                                                                                                        <script src="/ae/lg-story/assets/js/main.js"></script>
                                                                                                                                                                        <script src="/ae/lg-story/assets/scripts/gstring.js" type="text/javascript"></script>
                                                                                                                                                                        <jsp:include page="/WEB-INF/jsp/gp/common/include/tail/tail-script-default.jsp" /> 

                                                                                                                                                                        <script>
                                                                                                                                                                            function view_more(view_more_btn, show_content, view_less_btn) {
                                                                                                                                                                            document.getElementById(view_more_btn).style.visibility = "hidden";
                                                                                                                                                                            document.getElementById(show_content).style.display = "block";
                                                                                                                                                                            document.getElementById(view_less_btn).style.visibility = "visible";
                                                                                                                                                                            }
                                                                                                                                                                            function view_less(view_more_btn, show_content, view_less_btn) {
                                                                                                                                                                            document.getElementById(view_less_btn).style.visibility = "hidden";
                                                                                                                                                                            document.getElementById(show_content).style.display = "none";
                                                                                                                                                                            document.getElementById(view_more_btn).style.visibility = "visible";
                                                                                                                                                                            }
                                                                                                                                                                        </script>
                                                                                                                                                                        </body>
                                                                                                                                                                        </html>

"""