import streamlit as st
import json
st.title("personal library manager!")
st.write("welcome to your personal library manager!")


# availble book's, add book, remove book
menu = ["add book","available book's","remove book"]
choice = st.sidebar.selectbox("select an option", menu)

# add book
if choice == "add book":
   st.subheader("add a new book")
   title = st.text_input("title")
   author = st.text_input("author")
   publicatio_year = st.number_input("publication year")
   genre = st.text_input("genre")

   if st.button("add book"):
      add_book = (title,author,publicatio_year,genre)
      st.success(f"book {title} added succsessfully" )


# remove book
if choice == "remove book":
   st.subheader("remove book")
   title = st.text_input("title")
   author = st.text_input("author")
   publicatio_year = st.number_input("publication year")
   genre = st.text_input("genre")

   if st.button("remove book"):
      add_book = (title,author,publicatio_year,genre)
      st.success(f"book {title} remove succsessfully" )


# show available books
if st.button("available book"):
    books =["1- the Great Gatsby", "2- 1984"]
    st.success(books)


# user input for available book's
title=st.text_input("Enter the book title >> ")
st.text_input("Enter the author >> ")
st.number_input("Enter the publication year>> ")
st.text_input("Enter the genre>> ")
read=st.text_input("Have you read this book? yes/no")

book1= {
   
     "title" : "the Great Gatsby",
     "author" : "F. Scott Fitzgereld",
     "publication year" : 1925,
     "genre" : "Fiction",
     }
book2 = {
     "title" : "1984",
     "author" : "George orwell",
     "publication year" : 1949,
     "genre" : "Dystopian",
        
    }

# function for search books
def show_book(book1,book2):
   if choice == "the Great Gatsby":
    return(book1)
   if choice == "1984":
      return(book2)
   else:
       ("book is not availbe")
   if st.button("available book's"):
              show_book = (book1 , book2)
              st.success(f"open book's succsessfully{choice}")
 

#  button for search book
if st.button("search"):
   if title == "the Great Gatsby":
      result = book1
   elif title == "1984":
      result = book2
   else:
      result = "book not found"
   st.write(f"matching book: /n{result} - {read}")




            
             

   
        
     