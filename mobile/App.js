import React, { useMemo, useState } from 'react';
import { Alert, Image, Pressable, SafeAreaView, ScrollView, StyleSheet, Switch, Text, TextInput, View } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { Ionicons } from '@expo/vector-icons';
import Slider from '@react-native-community/slider';
import { Picker } from '@react-native-picker/picker';

const inspirations = [
  { id: 1, title: 'Planeje o seu dia', subtitle: 'Transforme objetivos grandes em ações possíveis.', image: 'https://images.unsplash.com/photo-1484480974693-6ca0a78fb36b?w=900', description: 'Começar o dia com um planejamento simples ajuda a visualizar prioridades e reduz a ansiedade. Escolha poucas tarefas realmente importantes, defina uma ordem possível e reserve pequenos intervalos para manter a energia até o fim.' },
  { id: 2, title: 'Organize seus estudos', subtitle: 'Constância vale mais do que longas maratonas.', image: 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=900', description: 'Uma rotina de estudos eficiente combina horários realistas, ambiente organizado e revisões frequentes. Dividir o conteúdo em blocos curtos facilita a concentração, melhora a retenção e permite acompanhar claramente o progresso realizado durante a semana.' },
  { id: 3, title: 'Trabalhe com foco', subtitle: 'Elimine distrações durante cada ciclo de atenção.', image: 'https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=900', description: 'Para trabalhar com foco, escolha uma tarefa, silencie notificações e determine um período específico de concentração. Ao terminar, faça uma pausa consciente antes de iniciar outra atividade, evitando alternâncias que consomem tempo e atenção.' },
  { id: 4, title: 'Cuide do seu equilíbrio', subtitle: 'Descanso também faz parte de uma boa rotina.', image: 'https://images.unsplash.com/photo-1506126613408-eca07ce68773?w=900', description: 'Produtividade sustentável depende de descanso, alimentação e movimento. Criar limites para o trabalho protege a saúde, melhora decisões e mantém a criatividade. Uma agenda equilibrada inclui compromissos pessoais com a mesma seriedade das entregas profissionais.' },
  { id: 5, title: 'Celebre seu progresso', subtitle: 'Reconheça cada etapa concluída no caminho.', image: 'https://images.unsplash.com/photo-1527529482837-4698179dc6ce?w=900', description: 'Registrar pequenas conquistas torna a evolução visível e fortalece a motivação. Ao concluir uma etapa, revise o que funcionou, reconheça o esforço investido e use esse aprendizado para definir o próximo objetivo com mais confiança.' },
];

const coverImage = 'https://images.unsplash.com/photo-1517842645767-c639042777db?w=1200';

function Header({ screen, onNavigate }) {
  return <View style={styles.header}>
    <View><Text style={styles.brand}>TASKTRACKER</Text><Text style={styles.headerTitle}>{screen === 'inspirations' ? 'Inspirações' : 'Planejador'}</Text></View>
    <Pressable style={styles.headerButton} onPress={() => onNavigate(screen === 'inspirations' ? 'planner' : 'inspirations')}><Ionicons name={screen === 'inspirations' ? 'options-outline' : 'images-outline'} size={24} color="#fff" /></Pressable>
  </View>;
}

function InspirationsScreen() {
  const [expandedId, setExpandedId] = useState(null);
  return <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
    <View style={styles.hero}><Image source={{ uri: coverImage }} style={styles.heroImage} /><View style={styles.heroOverlay}><Text style={styles.heroEyebrow}>SUA ROTINA, SEU RITMO</Text><Text style={styles.heroTitle}>Construa uma semana mais leve e produtiva.</Text></View></View>
    <Text style={styles.sectionTitle}>5 práticas para evoluir</Text><Text style={styles.sectionText}>Toque em uma opção para abrir a descrição completa.</Text>
    {inspirations.map((item) => {
      const expanded = expandedId === item.id;
      return <Pressable key={item.id} style={[styles.card, expanded && styles.cardExpanded]} onPress={() => setExpandedId(expanded ? null : item.id)}>
        <Image source={{ uri: item.image }} style={styles.cardImage} />
        <View style={styles.cardBody}><View style={styles.cardTitleRow}><Text style={styles.cardTitle}>{item.title}</Text><Ionicons name={expanded ? 'chevron-up' : 'chevron-down'} size={21} color="#6d4aff" /></View><Text style={styles.cardSubtitle}>{item.subtitle}</Text>{expanded && <Text style={styles.cardDescription}>{item.description}</Text>}</View>
      </Pressable>;
    })}
  </ScrollView>;
}

function Field({ label, value, onChangeText, placeholder }) {
  return <View style={styles.fieldGroup}><Text style={styles.label}>{label}</Text><TextInput style={styles.input} value={value} onChangeText={onChangeText} placeholder={placeholder} placeholderTextColor="#9b98aa" /></View>;
}

function PlannerScreen() {
  const [title, setTitle] = useState(''); const [description, setDescription] = useState('');
  const [date, setDate] = useState(''); const [responsible, setResponsible] = useState('');
  const [priority, setPriority] = useState('Média'); const [category, setCategory] = useState('Estudos');
  const [progress, setProgress] = useState(40); const [focusMinutes, setFocusMinutes] = useState(30);
  const [notifications, setNotifications] = useState(true); const [dailyReminder, setDailyReminder] = useState(false);
  const [message, setMessage] = useState('');
  const summary = useMemo(() => `${priority} • ${category} • ${Math.round(progress)}%`, [priority, category, progress]);

  function saveTask() {
    if (!title.trim() || !responsible.trim()) { Alert.alert('Campos necessários', 'Informe o título e o responsável pela tarefa.'); return; }
    setMessage(`Tarefa “${title.trim()}” salva com sucesso! ${summary}`);
  }
  function clearForm() {
    setTitle(''); setDescription(''); setDate(''); setResponsible(''); setPriority('Média'); setCategory('Estudos'); setProgress(40); setFocusMinutes(30); setNotifications(true); setDailyReminder(false); setMessage('Formulário limpo. Você pode criar uma nova tarefa.');
  }

  return <ScrollView contentContainerStyle={styles.scrollContent} keyboardShouldPersistTaps="handled">
    <View style={styles.formIntro}><Text style={styles.formIntroTitle}>Nova tarefa</Text><Text style={styles.formIntroText}>Preencha as preferências para organizar o próximo objetivo.</Text></View>
    <Field label="Título" value={title} onChangeText={setTitle} placeholder="Ex.: Revisar conteúdo" />
    <Field label="Descrição" value={description} onChangeText={setDescription} placeholder="Detalhes da atividade" />
    <Field label="Prazo" value={date} onChangeText={setDate} placeholder="DD/MM/AAAA" />
    <Field label="Responsável" value={responsible} onChangeText={setResponsible} placeholder="Nome do responsável" />
    <Text style={styles.label}>Prioridade</Text><View style={styles.pickerBox}><Picker selectedValue={priority} onValueChange={setPriority}><Picker.Item label="Baixa" value="Baixa" /><Picker.Item label="Média" value="Média" /><Picker.Item label="Alta" value="Alta" /></Picker></View>
    <Text style={styles.label}>Categoria</Text><View style={styles.pickerBox}><Picker selectedValue={category} onValueChange={setCategory}><Picker.Item label="Estudos" value="Estudos" /><Picker.Item label="Trabalho" value="Trabalho" /><Picker.Item label="Pessoal" value="Pessoal" /></Picker></View>
    <View style={styles.controlCard}>
      <View style={styles.controlHeading}><Text style={styles.label}>Progresso</Text><Text style={styles.value}>{Math.round(progress)}%</Text></View><Slider minimumValue={0} maximumValue={100} step={5} value={progress} onValueChange={setProgress} minimumTrackTintColor="#6d4aff" maximumTrackTintColor="#ded9f8" thumbTintColor="#6d4aff" />
      <View style={styles.controlHeading}><Text style={styles.label}>Tempo de foco</Text><Text style={styles.value}>{Math.round(focusMinutes)} min</Text></View><Slider minimumValue={15} maximumValue={120} step={5} value={focusMinutes} onValueChange={setFocusMinutes} minimumTrackTintColor="#ff8a5b" maximumTrackTintColor="#fde0d4" thumbTintColor="#ff8a5b" />
    </View>
    <View style={styles.switchRow}><View style={styles.switchText}><Text style={styles.label}>Notificações</Text><Text style={styles.helper}>Avisar sobre alterações na tarefa</Text></View><Switch value={notifications} onValueChange={setNotifications} trackColor={{ false: '#d9d7df', true: '#b9aaff' }} thumbColor={notifications ? '#6d4aff' : '#fff'} /></View>
    <View style={styles.switchRow}><View style={styles.switchText}><Text style={styles.label}>Lembrete diário</Text><Text style={styles.helper}>Relembrar a tarefa todos os dias</Text></View><Switch value={dailyReminder} onValueChange={setDailyReminder} trackColor={{ false: '#d9d7df', true: '#b9aaff' }} thumbColor={dailyReminder ? '#6d4aff' : '#fff'} /></View>
    {!!message && <Text style={styles.feedback}>{message}</Text>}
    <View style={styles.buttonRow}><Pressable style={[styles.actionButton, styles.secondaryButton]} onPress={clearForm}><Text style={styles.secondaryButtonText}>Limpar</Text></Pressable><Pressable style={[styles.actionButton, styles.primaryButton]} onPress={saveTask}><Text style={styles.primaryButtonText}>Salvar tarefa</Text></Pressable></View>
  </ScrollView>;
}

export default function App() {
  const [screen, setScreen] = useState('inspirations');
  return <SafeAreaView style={styles.safeArea}><StatusBar style="light" /><Header screen={screen} onNavigate={setScreen} />{screen === 'inspirations' ? <InspirationsScreen /> : <PlannerScreen />}<View style={styles.bottomNav}>
    <Pressable style={styles.navItem} onPress={() => setScreen('inspirations')}><Ionicons name={screen === 'inspirations' ? 'images' : 'images-outline'} size={22} color={screen === 'inspirations' ? '#6d4aff' : '#807d8d'} /><Text style={[styles.navText, screen === 'inspirations' && styles.navTextActive]}>Inspirações</Text></Pressable>
    <Pressable style={styles.navItem} onPress={() => setScreen('planner')}><Ionicons name={screen === 'planner' ? 'create' : 'create-outline'} size={22} color={screen === 'planner' ? '#6d4aff' : '#807d8d'} /><Text style={[styles.navText, screen === 'planner' && styles.navTextActive]}>Planejador</Text></Pressable>
  </View></SafeAreaView>;
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: '#f7f6fb' }, header: { backgroundColor: '#241f3d', paddingHorizontal: 22, paddingTop: 18, paddingBottom: 18, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' }, brand: { color: '#b9aaff', fontSize: 11, fontWeight: '800', letterSpacing: 2 }, headerTitle: { color: '#fff', fontSize: 24, fontWeight: '800', marginTop: 2 }, headerButton: { width: 44, height: 44, borderRadius: 14, backgroundColor: '#6d4aff', alignItems: 'center', justifyContent: 'center' },
  scrollContent: { padding: 18, paddingBottom: 110 }, hero: { height: 260, borderRadius: 24, overflow: 'hidden', backgroundColor: '#ddd', marginBottom: 24 }, heroImage: { width: '100%', height: '100%' }, heroOverlay: { position: 'absolute', left: 0, right: 0, bottom: 0, padding: 22, paddingTop: 70, backgroundColor: 'rgba(20,15,45,0.62)' }, heroEyebrow: { color: '#cfc5ff', fontSize: 11, fontWeight: '900', letterSpacing: 1.5 }, heroTitle: { color: '#fff', fontSize: 25, lineHeight: 31, fontWeight: '800', marginTop: 8 }, sectionTitle: { color: '#241f3d', fontSize: 22, fontWeight: '800' }, sectionText: { color: '#777386', fontSize: 14, marginTop: 5, marginBottom: 16 },
  card: { backgroundColor: '#fff', borderRadius: 20, marginBottom: 14, overflow: 'hidden', flexDirection: 'row', elevation: 2, shadowColor: '#2b234f', shadowOpacity: 0.08, shadowRadius: 12, shadowOffset: { width: 0, height: 5 } }, cardExpanded: { flexDirection: 'column' }, cardImage: { width: 112, minHeight: 116 }, cardBody: { flex: 1, padding: 16 }, cardTitleRow: { flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between', gap: 10 }, cardTitle: { color: '#2b2640', fontSize: 17, fontWeight: '800', flex: 1 }, cardSubtitle: { color: '#777386', fontSize: 13, lineHeight: 19, marginTop: 6 }, cardDescription: { color: '#4c4858', fontSize: 14, lineHeight: 22, marginTop: 13, borderTopWidth: 1, borderTopColor: '#eeeaf8', paddingTop: 13 },
  formIntro: { backgroundColor: '#6d4aff', padding: 20, borderRadius: 22, marginBottom: 20 }, formIntroTitle: { color: '#fff', fontSize: 22, fontWeight: '800' }, formIntroText: { color: '#e5e0ff', fontSize: 14, lineHeight: 20, marginTop: 5 }, fieldGroup: { marginBottom: 14 }, label: { color: '#302b43', fontSize: 14, fontWeight: '700', marginBottom: 7 }, input: { backgroundColor: '#fff', borderWidth: 1, borderColor: '#e5e2ed', height: 52, borderRadius: 14, paddingHorizontal: 15, color: '#241f3d', fontSize: 15 }, pickerBox: { backgroundColor: '#fff', borderWidth: 1, borderColor: '#e5e2ed', borderRadius: 14, overflow: 'hidden', marginBottom: 14 },
  controlCard: { backgroundColor: '#fff', padding: 17, borderRadius: 18, marginVertical: 6, gap: 4 }, controlHeading: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginTop: 6 }, value: { color: '#6d4aff', fontSize: 14, fontWeight: '800' }, switchRow: { backgroundColor: '#fff', borderRadius: 16, padding: 16, marginTop: 12, flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' }, switchText: { flex: 1, marginRight: 12 }, helper: { color: '#817d8d', fontSize: 12 }, feedback: { color: '#4e388f', backgroundColor: '#ebe6ff', borderRadius: 14, padding: 14, lineHeight: 20, marginTop: 16 },
  buttonRow: { flexDirection: 'row', gap: 12, marginTop: 18 }, actionButton: { flex: 1, height: 52, borderRadius: 15, alignItems: 'center', justifyContent: 'center' }, primaryButton: { backgroundColor: '#6d4aff' }, primaryButtonText: { color: '#fff', fontWeight: '800' }, secondaryButton: { borderWidth: 1.5, borderColor: '#6d4aff', backgroundColor: '#fff' }, secondaryButtonText: { color: '#6d4aff', fontWeight: '800' }, bottomNav: { position: 'absolute', left: 0, right: 0, bottom: 0, height: 78, backgroundColor: '#fff', borderTopWidth: 1, borderTopColor: '#e9e6ef', flexDirection: 'row', paddingBottom: 8 }, navItem: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 4 }, navText: { fontSize: 12, color: '#807d8d', fontWeight: '600' }, navTextActive: { color: '#6d4aff', fontWeight: '800' },
});
