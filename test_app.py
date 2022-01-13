import app

list_documents = ['passport "2207 876234" "Василий Гупкин"', 'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"']
new_guy = ['insurance', '12874', 'Венеамин Келлер', 4]
del_guy = '2207 876234'
class TestAppPytest:
    
    def test_add_doc(self):
        app.add_new_doc(new_guy[1], new_guy[0], new_guy[2], new_guy[3])
        assert app.get_doc_owner_name(new_guy[1]) == new_guy[2]
    
    def test_show_docs(self):
       assert app.show_all_docs_info() == list_documents
    
    def test_del_doc(self): 
        assert app.delete_doc(del_guy)
        
