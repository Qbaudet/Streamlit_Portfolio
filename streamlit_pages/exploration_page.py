import streamlit as st
from data_handling_and_plots import *
from streamlit_folium import st_folium


def show_data_exploration():
    df: DataFrame = load_dataset()
    df: DataFrame = data_preprocessing(df)
    st.markdown('''<h1 class="main-content"> Added value of <span style='color:#38b3fc;'>French High schools</span>! 🏫</h1>''',
                unsafe_allow_html=True)
    st.write("")
    st.markdown("""
    The dataset I’ve chosen is the <span style='color:#38b3fc; font-weight:bold;'>"Indicateurs de valeur ajoutée des lycées d'enseignement général et technologique"</span> dataset, which provides a precise look at how well high schools in France help their students succeed.  
    I picked this dataset because it goes beyond just showing baccalaureate pass rates since it actually highlights the impact each school has on student outcomes, by using an <span style='color:#38b3fc; font-weight:bold;'>added value metric</span>. It is calculated by finding the expected results of the school considering things like <span style='color:#38b3fc; font-weight:bold;'>student demographics</span> and <span style='color:#38b3fc; font-weight:bold;'>academic backgrounds</span>, and then compares it to the actual results to give a score.  
    In my opinion, it offers a more meaningful view of school performance because it takes into consideration the entire context instead of just looking at the numbers.
    
    It is thus perfect for exploring the way in which different french high schools contribute to the success of their students, with data ranging from 2013 to 2023.

    The dataset was taken from the <span style='color:#38b3fc; font-weight:bold;'>data.gouv</span> french website which is trustworthy, here is the link if you want to check it out! [Dataset](https://data.education.gouv.fr/explore/dataset/fr-en-indicateurs-de-resultat-des-lycees-gt_v2/information/?disjunctive.uai&disjunctive.secteur&disjunctive.libelle_commune&disjunctive.libelle_departement&disjunctive.libelle_academie&disjunctive.libelle_region&sort=num_ligne).
    """, unsafe_allow_html=True)
    st.write("")

    # Section 1: Analysis of the raw data
    show_dataset(df)

    # Section 2: Exploration of distributions
    show_distributions(df)

    # Section 3: Analysis of the tendencies
    show_tendencies(df)

    # Section 4: Case study for 2023
    show_case_study_2023(df)

    # Section 5: Case study for my high school: Talma
    show_case_study_talma(df)

    st.markdown(
        '''<h1 class="main-content"> <span style='color:#38b3fc;'>Conclusion</span>! 🏫</h1>''',
        unsafe_allow_html=True)
    st.write("")
    st.markdown("""
            From what we've seen during this data analysis, the <span style='color:#38b3fc;'>added value</span> is a difficult metric to analyse patterns from. Since it is calculated individualy based on the specific factors of each highschools, we cannot truly understand the meaning behind each of its values.
            However, we were able to pick up on a few overall trends during this exploration. 
            Namely, the <span style='color:#38b3fc;'>Covid-19</span> had a huge impact on the success rates of the baccalaureate exams, getting record scores. The situation is only progressively getting back to normal rates, but we can still see that overall the success rates and even the honours are higher than before.
               
            This can either indicate that the <span style='color:#38b3fc;'>exams got easier</span> with the introduction of continuous marking, but could also tell that <span style='color:#38b3fc;'>the students are getting better</span>.
        """, unsafe_allow_html=True)


def show_dataset(df: DataFrame):
    st.header("Let's start exploring the dataset! 📈")
    st.write("")
    st.write("")
    st.write("Here is what it looks like:")
    st.dataframe(df)
    st.write("")
    st.write("We have a few crucial information in this dataset. Each high school has the information needed to recognize it : its name, location but also a UAI number which is a unique identifier.")
    st.write("There is data present from the year 2013 to 2023 and for each year each high school has important data like success rate, added value, mention rate, and the differences between course of studies.")
    st.write("")


def show_distributions(df: DataFrame):
    st.header("Analysis of the different distributions:")
    st.write("")

    # First distribution plot
    st.subheader("Distribution of the baccalaureate success rate depending on the years:")

    # Slider to select the years
    years = df['Annee'].unique()
    selected_year = st.slider('Select the year', int(min(years)), int(max(years)), int(min(years)), key=1)
    columns_to_study = ['Annee', 'Taux de reussite - Toutes series']
    distribution_plot = create_distribution_plot(df, columns_to_study, selected_year)

    col1, col2 = st.columns([2, 1])  # Define two columns with different widths
    with col1:
        st.pyplot(distribution_plot)
    with col2:
        st.write(
            "From what we can see, it seems that the baccalaureate success rates have increased with the years, we observe more and more high schools with success rates > 97%.")
        st.write(
            "Indeed, we can see progressively that the graph get more and more fully concentrated to the very right, which means that the high schools are becoming more homogeneous with their success rates.")
        st.write(
            "2017 in particular has been a tough year seeing how there are almost as many highschools with >97% success rates than ones around 89%.")

    # Second distribution plot
    st.write("")
    st.subheader("Distribution of the added value on the success rate of the baccalaureate depending on the years:")

    # Slider to select the years
    years = df['Annee'].unique()
    selected_year = st.slider('Select the year', int(min(years)), int(max(years)), int(min(years)), key=2)
    columns_to_study = ['Annee', 'Valeur ajoutee du taux de reussite - Toutes series']
    distribution_plot = create_distribution_plot(df, columns_to_study, selected_year)

    col1, col2 = st.columns([2, 1])  # Define two columns with different widths
    with col1:
        st.pyplot(distribution_plot)
    with col2:
        st.write(
            "Concerning the added value that high schools have brought to the success rate of their students, we can see that their distributions follows a normal distribution, which was to be expected since there are some that bring a lot of values but others that are less impactful.")
        st.write(
            "We can also see that these distributions are also narrow, which means that it is uncommon for high schools to get an added value <-10 or >10.")
    st.write("")


def show_tendencies(df: DataFrame):
    st.header("Analysis of the tendencies over the years:")
    st.write("")

    st.subheader("Trends in the number of students, average success rate and average added value on the success rate:")
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("Average number of students:")
        trend_plot = create_trend_plot(df, "Presents - Toutes series")
        st.pyplot(trend_plot)
        st.write(
            "We can see that the number of students has risen significantly starting from 2018, which indicates that the high schools are getting fuller and fuller.")
    with col2:
        st.write("Average success rate for the final exam:")
        trend_plot = create_trend_plot(df, "Taux de reussite - Toutes series")
        st.pyplot(trend_plot)
        st.write(
            "We can see that the success rate used to be fixed at around 92%, but since 2020 it has shot up to be closer to 98%. This jump coincides with the Covid-19 which lead to the suppression of the exams, replaced by continuous grades. The two years where this was in place were the most successful.")
    with col3:
        st.write("Average added value on the success rate for high schools:")
        trend_plot = create_trend_plot(df, "Valeur ajoutee du taux de reussite - Toutes series")
        st.pyplot(trend_plot)
        st.write(
            "There doesn't really seem to be a trend in this data, it is difficult to interpret directly the added value without the details of the social conditions.")

    st.write("")
    st.subheader("Comparison between the public and private sector:")
    st.write("")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Success rate", "Added value to Success rate", "Honour rate", "Added value to honour rate"])

    with tab1:
        st.write("Success rate tendencies for the public and private field over the years:")
        box_plot = create_box_plot_type(df, "Taux de reussite - Toutes series")
        st.pyplot(box_plot)
        st.write(
            "From this, we can see that no matter the year, the average success rate at the baccalaureate exam is always higher for the private sector than the public.")

    with tab2:
        st.write("Added value to success rate tendencies for the public and private field over the years:")
        box_plot = create_box_plot_type(df, "Valeur ajoutee du taux de reussite - Toutes series")
        st.pyplot(box_plot)
        st.write(
            "From this graph, we can see a very clear pattern: the public high school's added value for the success rate is always negative, while the ones for the private sector are always positive. This means that the private sector manages to provide greater education which leads to better results than what is expected based on the profiles of their students.")

    with tab3:
        st.write("Honour rate tendencies for the public and private field over the years:")
        box_plot = create_box_plot_type(df, "Taux de mentions - Toutes series")
        st.pyplot(box_plot)
        st.write(
            "We can see that the honour rate has started to be put in the dataset starting from 2017. As for the trends, we can see that the private schools always end up having a higher honour rate than the public ones. They always lead by around 10% honour rate.")

    with tab4:
        st.write("Added value to the honour rate for the public and private field over the years:")
        box_plot = create_box_plot_type(df, "Valeur ajoutee du taux de mentions - Toutes series")
        st.pyplot(box_plot)
        st.write(
            "Even when taking into consideration the social factors and profile of the students, the private sector still leads, always bringing positive added value on the honour rate. On the contrary, the public sector is not doing great by not gathering as many honours as it should considering the context.")

    st.write("")
    st.write(
        "Therefore, it is safe to say that private schools truly bring the best out of their students, they achieve the best results when compared to the public field.")
    st.write("")
    st.write("")


def show_case_study_2023(df: DataFrame):
    st.header("Case study for the year 2023:")
    st.write("")

    st.subheader("Pie charts on the proportion of honours in the general and technological fields of study:")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("Trends for the honours for the general course of studies:")
        trends_plot = create_pie_chart_2023(df, ["Nombre de mentions TB avec felicitations - G",
                                                 "Nombre de mentions TB sans felicitations - G",
                                                 "Nombre de mentions B - G", "Nombre de mentions AB - G"])
        st.pyplot(trends_plot)

    with col2:
        st.write("Trends for the honours for the technological course of studies:")
        trends_plot = create_pie_chart_2023(df, ["Nombre de mentions TB avec felicitations - T",
                                                 "Nombre de mentions TB sans felicitations - T",
                                                 "Nombre de mentions B - T", "Nombre de mentions AB - T"])
        st.pyplot(trends_plot)

    st.write(
        "We can see from those two pie charts that the most common honour is 'Assez bien'. The general course of studies has a greater proportion of TB and B honours, while 63% of hounours in the technological field are AB.")
    st.write("")

    st.write("")
    st.subheader("Added value on of the french departments in 2023:")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.write("French map of the added value on the success rate:")
        map_1 = create_department_success_rate_map(df, "Valeur ajoutee du taux de reussite - Toutes series")
        st_data_1 = st_folium(map_1, height=600)
        st.write(
            "From what we can see in this map, there isn't truly any department which is the best or the worst. All of the averages of the added values per departement are pretty similar. The one with the highest average is 'Hauts de Corse', while the lowest is the 'Haute-Saône'")

    with col2:
        st.write("French map of the added value on the honour rate:")
        map_2 = create_department_success_rate_map(df, "Valeur ajoutee du taux de mentions - Toutes series")
        st_data_2 = st_folium(map_2, height=600)
        st.write(
            "In this map, the differences between departments are a bit more striking. Once again, the 'Haute-Corse' is brings the highest added value, and we can notice that the departments in the very north, east and south tend to do better than the central ones. The departement which brings the lowest average of added value on the honours is the 'Cantal'.")

    st.write("")
    st.write(
        "From these two maps, we can see that the trend regarding which department brings the most added value overall is blurry. However, some departments stand out, especially the ones from the 'Corse'.")

    st.write("")


def show_case_study_talma(df: DataFrame):
    st.header("Case study on my personal high school : Lycée Talma:")
    st.write("")

    col1, col2 = st.columns([1, 3])
    with col1:
        option = st.radio("Select which plot to display:",
                          ("Rates", "Added Values", "Number of students")
                          )

    with col2:
        if option == "Rates":
            st.write("Trends on the rates of success and honours:")
            trend_plot_talma = create_trends_rates_talma(df, ["Taux de reussite - Toutes series",
                                                              "Taux de mentions - Toutes series"])
            st.pyplot(trend_plot_talma)

        elif option == "Added Values":
            st.write("Trends on the added values on success and honours:")
            trend_plot_talma = create_trends_added_values_talma(df,
                                                                ["Valeur ajoutee du taux de reussite - Toutes series",
                                                                 "Valeur ajoutee du taux de mentions - Toutes series"])
            st.pyplot(trend_plot_talma)

        elif option == "Number of students":
            st.write("Trend on the number of students over the years")
            trend_plot_talma = create_trend_number_students_talma(df, "Presents - Toutes series")
            st.pyplot(trend_plot_talma)

    st.write("")
    st.write(
        "From what we can see, my high school's results were influenced a lot by the Covid-19. Better success rates, more honours and added values, they got good results because of it. We can see that before that time the school didn't have great results with negative added values. Since the Covid however the results seem to slowly go back down, which is a bad sign, especially since the number of students is rising.")
    st.write("")