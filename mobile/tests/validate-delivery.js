const fs = require('fs');
const path = require('path');

const app = fs.readFileSync(path.join(__dirname, '..', 'App.js'), 'utf8');
const checks = [
  ['cinco itens na lista', (app.match(/description: '/g) || []).length === 5],
  ['seis imagens', (app.match(/images\.unsplash\.com/g) || []).length === 6],
  ['quatro inputs', (app.match(/<Field /g) || []).length === 4],
  ['dois pickers', (app.match(/<Picker selectedValue=/g) || []).length === 2],
  ['dois sliders', (app.match(/<Slider /g) || []).length === 2],
  ['dois switches', (app.match(/<Switch /g) || []).length === 2],
  ['dois botões de formulário', app.includes('onPress={clearForm}') && app.includes('onPress={saveTask}')],
  ['duas telas', app.includes('<InspirationsScreen />') && app.includes('<PlannerScreen />')],
];

for (const [name, passed] of checks) {
  if (!passed) throw new Error(`Falha: ${name}`);
  console.log(`✓ ${name}`);
}

const descriptions = [...app.matchAll(/description: '([^']+)'/g)].map((match) => match[1]);
for (const [index, value] of descriptions.entries()) {
  const words = value.trim().split(/\s+/).length;
  if (words < 30) throw new Error(`Descrição ${index + 1} possui somente ${words} palavras`);
}
const total = descriptions.join(' ').trim().split(/\s+/).length;
if (total < 150) throw new Error(`Total insuficiente: ${total} palavras`);
console.log(`✓ descrições: ${total} palavras no total e mínimo individual atendido`);
