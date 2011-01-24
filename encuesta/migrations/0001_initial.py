# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Encuestador'
        db.create_table('encuesta_encuestador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_completo', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('telefono', self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True)),
        ))
        db.send_create_signal('encuesta', ['Encuestador'])

        # Adding model 'Contraparte'
        db.create_table('encuesta_contraparte', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
        ))
        db.send_create_signal('encuesta', ['Contraparte'])

        # Adding model 'ViveCon'
        db.create_table('encuesta_vivecon', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('encuesta', ['ViveCon'])

        # Adding model 'ComposicionHogar'
        db.create_table('encuesta_composicionhogar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('tiene_pareja', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('cuantos_viven', self.gf('django.db.models.fields.IntegerField')()),
            ('entre0y6', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('entre7y17', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('entre18ymas', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('tiene_hijos', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('hijos0y6', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hijos7y17', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hijos18ymas', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('encuesta', ['ComposicionHogar'])

        # Adding M2M table for field vive_con on 'ComposicionHogar'
        db.create_table('encuesta_composicionhogar_vive_con', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('composicionhogar', models.ForeignKey(orm['encuesta.composicionhogar'], null=False)),
            ('vivecon', models.ForeignKey(orm['encuesta.vivecon'], null=False))
        ))
        db.create_unique('encuesta_composicionhogar_vive_con', ['composicionhogar_id', 'vivecon_id'])

        # Adding model 'LugarDeTrabajo'
        db.create_table('encuesta_lugardetrabajo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('encuesta', ['LugarDeTrabajo'])

        # Adding model 'Aporta'
        db.create_table('encuesta_aporta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('encuesta', ['Aporta'])

        # Adding model 'InformacionSocioEconomica'
        db.create_table('encuesta_informacionsocioeconomica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('estudia', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('nivel_educativo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('trabaja_fuera', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('hace_dinero', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuesta', ['InformacionSocioEconomica'])

        # Adding M2M table for field donde_trabaja on 'InformacionSocioEconomica'
        db.create_table('encuesta_informacionsocioeconomica_donde_trabaja', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('informacionsocioeconomica', models.ForeignKey(orm['encuesta.informacionsocioeconomica'], null=False)),
            ('lugardetrabajo', models.ForeignKey(orm['encuesta.lugardetrabajo'], null=False))
        ))
        db.create_unique('encuesta_informacionsocioeconomica_donde_trabaja', ['informacionsocioeconomica_id', 'lugardetrabajo_id'])

        # Adding M2M table for field aportan on 'InformacionSocioEconomica'
        db.create_table('encuesta_informacionsocioeconomica_aportan', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('informacionsocioeconomica', models.ForeignKey(orm['encuesta.informacionsocioeconomica'], null=False)),
            ('aporta', models.ForeignKey(orm['encuesta.aporta'], null=False))
        ))
        db.create_unique('encuesta_informacionsocioeconomica_aportan', ['informacionsocioeconomica_id', 'aporta_id'])

        # Adding model 'Recurso'
        db.create_table('encuesta_recurso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('encuesta', ['Recurso'])

        # Adding model 'AccesoControlRecurso'
        db.create_table('encuesta_accesocontrolrecurso', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
        ))
        db.send_create_signal('encuesta', ['AccesoControlRecurso'])

        # Adding M2M table for field recursos on 'AccesoControlRecurso'
        db.create_table('encuesta_accesocontrolrecurso_recursos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocontrolrecurso', models.ForeignKey(orm['encuesta.accesocontrolrecurso'], null=False)),
            ('recurso', models.ForeignKey(orm['encuesta.recurso'], null=False))
        ))
        db.create_unique('encuesta_accesocontrolrecurso_recursos', ['accesocontrolrecurso_id', 'recurso_id'])

        # Adding M2M table for field recursos_decide on 'AccesoControlRecurso'
        db.create_table('encuesta_accesocontrolrecurso_recursos_decide', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocontrolrecurso', models.ForeignKey(orm['encuesta.accesocontrolrecurso'], null=False)),
            ('recurso', models.ForeignKey(orm['encuesta.recurso'], null=False))
        ))
        db.create_unique('encuesta_accesocontrolrecurso_recursos_decide', ['accesocontrolrecurso_id', 'recurso_id'])

        # Adding model 'VBG'
        db.create_table('encuesta_vbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('encuesta', ['VBG'])

        # Adding model 'ConceptoViolencia'
        db.create_table('encuesta_conceptoviolencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
        ))
        db.send_create_signal('encuesta', ['ConceptoViolencia'])

        # Adding M2M table for field conocimientoVBG on 'ConceptoViolencia'
        db.create_table('encuesta_conceptoviolencia_conocimientoVBG', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('conceptoviolencia', models.ForeignKey(orm['encuesta.conceptoviolencia'], null=False)),
            ('vbg', models.ForeignKey(orm['encuesta.vbg'], null=False))
        ))
        db.create_unique('encuesta_conceptoviolencia_conocimientoVBG', ['conceptoviolencia_id', 'vbg_id'])

        # Adding model 'ExpresionVBG'
        db.create_table('encuesta_expresionvbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('maneras', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('encuesta', ['ExpresionVBG'])

        # Adding model 'Creencia'
        db.create_table('encuesta_creencia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('creencia', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuesta', ['Creencia'])

        # Adding model 'JustificacionVBG'
        db.create_table('encuesta_justificacionvbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('justificacion', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('encuesta', ['JustificacionVBG'])

        # Adding model 'CausaVBG'
        db.create_table('encuesta_causavbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('causa', self.gf('django.db.models.fields.IntegerField')()),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('encuesta', ['CausaVBG'])

        # Adding model 'SituacionVBG'
        db.create_table('encuesta_situacionvbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('conoce_hombres', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('conoce_mujeres', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('encuesta', ['SituacionVBG'])

        # Adding model 'BuscarAyuda'
        db.create_table('encuesta_buscarayuda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('encuesta', ['BuscarAyuda'])

        # Adding model 'QueDebeHacer'
        db.create_table('encuesta_quedebehacer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('encuesta', ['QueDebeHacer'])

        # Adding model 'AccionVBG'
        db.create_table('encuesta_accionvbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('ha_ayudado', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('encuesta', ['AccionVBG'])

        # Adding M2M table for field donde_buscar on 'AccionVBG'
        db.create_table('encuesta_accionvbg_donde_buscar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accionvbg', models.ForeignKey(orm['encuesta.accionvbg'], null=False)),
            ('buscarayuda', models.ForeignKey(orm['encuesta.buscarayuda'], null=False))
        ))
        db.create_unique('encuesta_accionvbg_donde_buscar', ['accionvbg_id', 'buscarayuda_id'])

        # Adding M2M table for field accion_tomar on 'AccionVBG'
        db.create_table('encuesta_accionvbg_accion_tomar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accionvbg', models.ForeignKey(orm['encuesta.accionvbg'], null=False)),
            ('quedebehacer', models.ForeignKey(orm['encuesta.quedebehacer'], null=False))
        ))
        db.create_unique('encuesta_accionvbg_accion_tomar', ['accionvbg_id', 'quedebehacer_id'])

        # Adding model 'QueHaceUd'
        db.create_table('encuesta_quehaceud', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accionvbg', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.AccionVBG'])),
            ('que_hace', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuesta', ['QueHaceUd'])

        # Adding model 'Quien'
        db.create_table('encuesta_quien', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('encuesta', ['Quien'])

        # Adding model 'PrevalenciaVBG'
        db.create_table('encuesta_prevalenciavbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('ha_vivido_vbg', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('que_tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('frecuencia', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuesta', ['PrevalenciaVBG'])

        # Adding M2M table for field quien on 'PrevalenciaVBG'
        db.create_table('encuesta_prevalenciavbg_quien', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('prevalenciavbg', models.ForeignKey(orm['encuesta.prevalenciavbg'], null=False)),
            ('quien', models.ForeignKey(orm['encuesta.quien'], null=False))
        ))
        db.create_unique('encuesta_prevalenciavbg_quien', ['prevalenciavbg_id', 'quien_id'])

        # Adding model 'ResolverVBG'
        db.create_table('encuesta_resolvervbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('encuesta', ['ResolverVBG'])

        # Adding model 'AsuntoPublicoVBG'
        db.create_table('encuesta_asuntopublicovbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
        ))
        db.send_create_signal('encuesta', ['AsuntoPublicoVBG'])

        # Adding M2M table for field resolverse_con on 'AsuntoPublicoVBG'
        db.create_table('encuesta_asuntopublicovbg_resolverse_con', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('asuntopublicovbg', models.ForeignKey(orm['encuesta.asuntopublicovbg'], null=False)),
            ('resolvervbg', models.ForeignKey(orm['encuesta.resolvervbg'], null=False))
        ))
        db.create_unique('encuesta_asuntopublicovbg_resolverse_con', ['asuntopublicovbg_id', 'resolvervbg_id'])

        # Adding model 'ComoAfecta'
        db.create_table('encuesta_comoafecta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('encuesta', ['ComoAfecta'])

        # Adding model 'EfectoVBG'
        db.create_table('encuesta_efectovbg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('afecta_mujeres', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('encuesta', ['EfectoVBG'])

        # Adding M2M table for field como_afecta on 'EfectoVBG'
        db.create_table('encuesta_efectovbg_como_afecta', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('efectovbg', models.ForeignKey(orm['encuesta.efectovbg'], null=False)),
            ('comoafecta', models.ForeignKey(orm['encuesta.comoafecta'], null=False))
        ))
        db.create_unique('encuesta_efectovbg_como_afecta', ['efectovbg_id', 'comoafecta_id'])

        # Adding model 'ConocimientoLey'
        db.create_table('encuesta_conocimientoley', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('existe_ley', self.gf('django.db.models.fields.IntegerField')()),
            ('mencione', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
        ))
        db.send_create_signal('encuesta', ['ConocimientoLey'])

        # Adding model 'AccionProhibida'
        db.create_table('encuesta_accionprohibida', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('padre_golpea', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('maestro_castiga', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('maestro_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('joven_case', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('joven_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('patron_acoso', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('lider_religioso', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('adulto_relacion', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('adulto_dinero', self.gf('django.db.models.fields.IntegerField')(default=4, blank=True)),
            ('conocimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.ConocimientoLey'])),
        ))
        db.send_create_signal('encuesta', ['AccionProhibida'])

        # Adding model 'Decision'
        db.create_table('encuesta_decision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('encuesta', ['Decision'])

        # Adding model 'TomaDecision'
        db.create_table('encuesta_tomadecision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
        ))
        db.send_create_signal('encuesta', ['TomaDecision'])

        # Adding M2M table for field decision on 'TomaDecision'
        db.create_table('encuesta_tomadecision_decision', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tomadecision', models.ForeignKey(orm['encuesta.tomadecision'], null=False)),
            ('decision', models.ForeignKey(orm['encuesta.decision'], null=False))
        ))
        db.create_unique('encuesta_tomadecision_decision', ['tomadecision_id', 'decision_id'])

        # Adding model 'Espacio'
        db.create_table('encuesta_espacio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('encuesta', ['Espacio'])

        # Adding model 'MotivoParticipacion'
        db.create_table('encuesta_motivoparticipacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('encuesta', ['MotivoParticipacion'])

        # Adding model 'ParticipacionPublica'
        db.create_table('encuesta_participacionpublica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
        ))
        db.send_create_signal('encuesta', ['ParticipacionPublica'])

        # Adding M2M table for field espacio on 'ParticipacionPublica'
        db.create_table('encuesta_participacionpublica_espacio', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participacionpublica', models.ForeignKey(orm['encuesta.participacionpublica'], null=False)),
            ('espacio', models.ForeignKey(orm['encuesta.espacio'], null=False))
        ))
        db.create_unique('encuesta_participacionpublica_espacio', ['participacionpublica_id', 'espacio_id'])

        # Adding M2M table for field motivo on 'ParticipacionPublica'
        db.create_table('encuesta_participacionpublica_motivo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('participacionpublica', models.ForeignKey(orm['encuesta.participacionpublica'], null=False)),
            ('motivoparticipacion', models.ForeignKey(orm['encuesta.motivoparticipacion'], null=False))
        ))
        db.create_unique('encuesta_participacionpublica_motivo', ['participacionpublica_id', 'motivoparticipacion_id'])

        # Adding model 'IncidenciaPolitica'
        db.create_table('encuesta_incidenciapolitica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('existen_mujeres', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('satisfecha', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuesta', ['IncidenciaPolitica'])

        # Adding model 'CalidadAtencion'
        db.create_table('encuesta_calidadatencion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('valor_servicio', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuesta', ['CalidadAtencion'])

        # Adding model 'Propuesta'
        db.create_table('encuesta_propuesta', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('propuesta', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('si_tipo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('no_porque', self.gf('django.db.models.fields.TextField')()),
            ('calidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.CalidadAtencion'])),
        ))
        db.send_create_signal('encuesta', ['Propuesta'])

        # Adding model 'PropuestaNegociada'
        db.create_table('encuesta_propuestanegociada', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('propuesta', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('si_tipo', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('no_porque', self.gf('django.db.models.fields.TextField')()),
            ('calidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.CalidadAtencion'])),
        ))
        db.send_create_signal('encuesta', ['PropuestaNegociada'])

        # Adding model 'Corresponsabilidad'
        db.create_table('encuesta_corresponsabilidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('lavar', self.gf('django.db.models.fields.IntegerField')()),
            ('plancar', self.gf('django.db.models.fields.IntegerField')()),
            ('limpiar', self.gf('django.db.models.fields.IntegerField')()),
            ('jalar_agua', self.gf('django.db.models.fields.IntegerField')()),
            ('cuidar_ninos', self.gf('django.db.models.fields.IntegerField')()),
            ('hacer_mandados', self.gf('django.db.models.fields.IntegerField')()),
            ('llevar_lena', self.gf('django.db.models.fields.IntegerField')()),
            ('lavar_trastes', self.gf('django.db.models.fields.IntegerField')()),
            ('arreglar_cama', self.gf('django.db.models.fields.IntegerField')()),
            ('ir_reuniones', self.gf('django.db.models.fields.IntegerField')()),
            ('acompanar', self.gf('django.db.models.fields.IntegerField')()),
            ('hacer_compras', self.gf('django.db.models.fields.IntegerField')()),
            ('pagar_servicios', self.gf('django.db.models.fields.IntegerField')()),
            ('llevar_enfermos', self.gf('django.db.models.fields.IntegerField')()),
            ('cuidar_enfermos', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('encuesta', ['Corresponsabilidad'])

        # Adding model 'SolucionConflicto'
        db.create_table('encuesta_solucionconflicto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('encuesta', ['SolucionConflicto'])

        # Adding model 'NegociacionExitosa'
        db.create_table('encuesta_negociacionexitosa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('encuesta', ['NegociacionExitosa'])

        # Adding model 'ComunicacionAsertiva'
        db.create_table('encuesta_comunicacionasertiva', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
        ))
        db.send_create_signal('encuesta', ['ComunicacionAsertiva'])

        # Adding M2M table for field identifico on 'ComunicacionAsertiva'
        db.create_table('encuesta_comunicacionasertiva_identifico', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comunicacionasertiva', models.ForeignKey(orm['encuesta.comunicacionasertiva'], null=False)),
            ('solucionconflicto', models.ForeignKey(orm['encuesta.solucionconflicto'], null=False))
        ))
        db.create_unique('encuesta_comunicacionasertiva_identifico', ['comunicacionasertiva_id', 'solucionconflicto_id'])

        # Adding M2M table for field negociacion_exitosa on 'ComunicacionAsertiva'
        db.create_table('encuesta_comunicacionasertiva_negociacion_exitosa', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('comunicacionasertiva', models.ForeignKey(orm['encuesta.comunicacionasertiva'], null=False)),
            ('negociacionexitosa', models.ForeignKey(orm['encuesta.negociacionexitosa'], null=False))
        ))
        db.create_unique('encuesta_comunicacionasertiva_negociacion_exitosa', ['comunicacionasertiva_id', 'negociacionexitosa_id'])

        # Adding model 'Mujer'
        db.create_table('encuesta_mujer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
            ('comunidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Comunidad'])),
            ('municipio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Municipio'])),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lugar_origen', self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True)),
            ('asiste_iglesia', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cual_iglesia', self.gf('django.db.models.fields.CharField')(default='', max_length=150, blank=True)),
            ('encuestador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Encuestador'])),
            ('contraparte', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['encuesta.Contraparte'])),
        ))
        db.send_create_signal('encuesta', ['Mujer'])


    def backwards(self, orm):
        
        # Deleting model 'Encuestador'
        db.delete_table('encuesta_encuestador')

        # Deleting model 'Contraparte'
        db.delete_table('encuesta_contraparte')

        # Deleting model 'ViveCon'
        db.delete_table('encuesta_vivecon')

        # Deleting model 'ComposicionHogar'
        db.delete_table('encuesta_composicionhogar')

        # Removing M2M table for field vive_con on 'ComposicionHogar'
        db.delete_table('encuesta_composicionhogar_vive_con')

        # Deleting model 'LugarDeTrabajo'
        db.delete_table('encuesta_lugardetrabajo')

        # Deleting model 'Aporta'
        db.delete_table('encuesta_aporta')

        # Deleting model 'InformacionSocioEconomica'
        db.delete_table('encuesta_informacionsocioeconomica')

        # Removing M2M table for field donde_trabaja on 'InformacionSocioEconomica'
        db.delete_table('encuesta_informacionsocioeconomica_donde_trabaja')

        # Removing M2M table for field aportan on 'InformacionSocioEconomica'
        db.delete_table('encuesta_informacionsocioeconomica_aportan')

        # Deleting model 'Recurso'
        db.delete_table('encuesta_recurso')

        # Deleting model 'AccesoControlRecurso'
        db.delete_table('encuesta_accesocontrolrecurso')

        # Removing M2M table for field recursos on 'AccesoControlRecurso'
        db.delete_table('encuesta_accesocontrolrecurso_recursos')

        # Removing M2M table for field recursos_decide on 'AccesoControlRecurso'
        db.delete_table('encuesta_accesocontrolrecurso_recursos_decide')

        # Deleting model 'VBG'
        db.delete_table('encuesta_vbg')

        # Deleting model 'ConceptoViolencia'
        db.delete_table('encuesta_conceptoviolencia')

        # Removing M2M table for field conocimientoVBG on 'ConceptoViolencia'
        db.delete_table('encuesta_conceptoviolencia_conocimientoVBG')

        # Deleting model 'ExpresionVBG'
        db.delete_table('encuesta_expresionvbg')

        # Deleting model 'Creencia'
        db.delete_table('encuesta_creencia')

        # Deleting model 'JustificacionVBG'
        db.delete_table('encuesta_justificacionvbg')

        # Deleting model 'CausaVBG'
        db.delete_table('encuesta_causavbg')

        # Deleting model 'SituacionVBG'
        db.delete_table('encuesta_situacionvbg')

        # Deleting model 'BuscarAyuda'
        db.delete_table('encuesta_buscarayuda')

        # Deleting model 'QueDebeHacer'
        db.delete_table('encuesta_quedebehacer')

        # Deleting model 'AccionVBG'
        db.delete_table('encuesta_accionvbg')

        # Removing M2M table for field donde_buscar on 'AccionVBG'
        db.delete_table('encuesta_accionvbg_donde_buscar')

        # Removing M2M table for field accion_tomar on 'AccionVBG'
        db.delete_table('encuesta_accionvbg_accion_tomar')

        # Deleting model 'QueHaceUd'
        db.delete_table('encuesta_quehaceud')

        # Deleting model 'Quien'
        db.delete_table('encuesta_quien')

        # Deleting model 'PrevalenciaVBG'
        db.delete_table('encuesta_prevalenciavbg')

        # Removing M2M table for field quien on 'PrevalenciaVBG'
        db.delete_table('encuesta_prevalenciavbg_quien')

        # Deleting model 'ResolverVBG'
        db.delete_table('encuesta_resolvervbg')

        # Deleting model 'AsuntoPublicoVBG'
        db.delete_table('encuesta_asuntopublicovbg')

        # Removing M2M table for field resolverse_con on 'AsuntoPublicoVBG'
        db.delete_table('encuesta_asuntopublicovbg_resolverse_con')

        # Deleting model 'ComoAfecta'
        db.delete_table('encuesta_comoafecta')

        # Deleting model 'EfectoVBG'
        db.delete_table('encuesta_efectovbg')

        # Removing M2M table for field como_afecta on 'EfectoVBG'
        db.delete_table('encuesta_efectovbg_como_afecta')

        # Deleting model 'ConocimientoLey'
        db.delete_table('encuesta_conocimientoley')

        # Deleting model 'AccionProhibida'
        db.delete_table('encuesta_accionprohibida')

        # Deleting model 'Decision'
        db.delete_table('encuesta_decision')

        # Deleting model 'TomaDecision'
        db.delete_table('encuesta_tomadecision')

        # Removing M2M table for field decision on 'TomaDecision'
        db.delete_table('encuesta_tomadecision_decision')

        # Deleting model 'Espacio'
        db.delete_table('encuesta_espacio')

        # Deleting model 'MotivoParticipacion'
        db.delete_table('encuesta_motivoparticipacion')

        # Deleting model 'ParticipacionPublica'
        db.delete_table('encuesta_participacionpublica')

        # Removing M2M table for field espacio on 'ParticipacionPublica'
        db.delete_table('encuesta_participacionpublica_espacio')

        # Removing M2M table for field motivo on 'ParticipacionPublica'
        db.delete_table('encuesta_participacionpublica_motivo')

        # Deleting model 'IncidenciaPolitica'
        db.delete_table('encuesta_incidenciapolitica')

        # Deleting model 'CalidadAtencion'
        db.delete_table('encuesta_calidadatencion')

        # Deleting model 'Propuesta'
        db.delete_table('encuesta_propuesta')

        # Deleting model 'PropuestaNegociada'
        db.delete_table('encuesta_propuestanegociada')

        # Deleting model 'Corresponsabilidad'
        db.delete_table('encuesta_corresponsabilidad')

        # Deleting model 'SolucionConflicto'
        db.delete_table('encuesta_solucionconflicto')

        # Deleting model 'NegociacionExitosa'
        db.delete_table('encuesta_negociacionexitosa')

        # Deleting model 'ComunicacionAsertiva'
        db.delete_table('encuesta_comunicacionasertiva')

        # Removing M2M table for field identifico on 'ComunicacionAsertiva'
        db.delete_table('encuesta_comunicacionasertiva_identifico')

        # Removing M2M table for field negociacion_exitosa on 'ComunicacionAsertiva'
        db.delete_table('encuesta_comunicacionasertiva_negociacion_exitosa')

        # Deleting model 'Mujer'
        db.delete_table('encuesta_mujer')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.accesocontrolrecurso': {
            'Meta': {'object_name': 'AccesoControlRecurso'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'recursos-propios'", 'symmetrical': 'False', 'to': "orm['encuesta.Recurso']"}),
            'recursos_decide': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'recursos-decide'", 'symmetrical': 'False', 'to': "orm['encuesta.Recurso']"})
        },
        'encuesta.accionprohibida': {
            'Meta': {'object_name': 'AccionProhibida'},
            'adulto_dinero': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'adulto_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'conocimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.ConocimientoLey']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'joven_case': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'joven_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'lider_religioso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_castiga': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'maestro_relacion': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'padre_golpea': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'}),
            'patron_acoso': ('django.db.models.fields.IntegerField', [], {'default': '4', 'blank': 'True'})
        },
        'encuesta.accionvbg': {
            'Meta': {'object_name': 'AccionVBG'},
            'accion_tomar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.QueDebeHacer']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_buscar': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.BuscarAyuda']", 'symmetrical': 'False'}),
            'ha_ayudado': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.aporta': {
            'Meta': {'object_name': 'Aporta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.asuntopublicovbg': {
            'Meta': {'object_name': 'AsuntoPublicoVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'resolverse_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ResolverVBG']", 'symmetrical': 'False'})
        },
        'encuesta.buscarayuda': {
            'Meta': {'object_name': 'BuscarAyuda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.calidadatencion': {
            'Meta': {'object_name': 'CalidadAtencion'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'valor_servicio': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.causavbg': {
            'Meta': {'object_name': 'CausaVBG'},
            'causa': ('django.db.models.fields.IntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.comoafecta': {
            'Meta': {'object_name': 'ComoAfecta'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.composicionhogar': {
            'Meta': {'object_name': 'ComposicionHogar'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuantos_viven': ('django.db.models.fields.IntegerField', [], {}),
            'entre0y6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entre18ymas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'entre7y17': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos0y6': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos18ymas': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'hijos7y17': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'tiene_hijos': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'tiene_pareja': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'vive_con': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ViveCon']", 'symmetrical': 'False'})
        },
        'encuesta.comunicacionasertiva': {
            'Meta': {'object_name': 'ComunicacionAsertiva'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifico': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.SolucionConflicto']", 'symmetrical': 'False'}),
            'negociacion_exitosa': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.NegociacionExitosa']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.conceptoviolencia': {
            'Meta': {'object_name': 'ConceptoViolencia'},
            'conocimientoVBG': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.VBG']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.conocimientoley': {
            'Meta': {'object_name': 'ConocimientoLey'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existe_ley': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mencione': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.contraparte': {
            'Meta': {'object_name': 'Contraparte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'})
        },
        'encuesta.corresponsabilidad': {
            'Meta': {'object_name': 'Corresponsabilidad'},
            'acompanar': ('django.db.models.fields.IntegerField', [], {}),
            'arreglar_cama': ('django.db.models.fields.IntegerField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'cuidar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'cuidar_ninos': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_compras': ('django.db.models.fields.IntegerField', [], {}),
            'hacer_mandados': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ir_reuniones': ('django.db.models.fields.IntegerField', [], {}),
            'jalar_agua': ('django.db.models.fields.IntegerField', [], {}),
            'lavar': ('django.db.models.fields.IntegerField', [], {}),
            'lavar_trastes': ('django.db.models.fields.IntegerField', [], {}),
            'limpiar': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_enfermos': ('django.db.models.fields.IntegerField', [], {}),
            'llevar_lena': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'pagar_servicios': ('django.db.models.fields.IntegerField', [], {}),
            'plancar': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.creencia': {
            'Meta': {'object_name': 'Creencia'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'creencia': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.decision': {
            'Meta': {'object_name': 'Decision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.efectovbg': {
            'Meta': {'object_name': 'EfectoVBG'},
            'afecta_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'como_afecta': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.ComoAfecta']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.encuestador': {
            'Meta': {'object_name': 'Encuestador'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_completo': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20', 'blank': 'True'})
        },
        'encuesta.espacio': {
            'Meta': {'object_name': 'Espacio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.expresionvbg': {
            'Meta': {'object_name': 'ExpresionVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maneras': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'encuesta.incidenciapolitica': {
            'Meta': {'object_name': 'IncidenciaPolitica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'existen_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'satisfecha': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.informacionsocioeconomica': {
            'Meta': {'object_name': 'InformacionSocioEconomica'},
            'aportan': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Aporta']", 'symmetrical': 'False'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'donde_trabaja': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.LugarDeTrabajo']", 'symmetrical': 'False'}),
            'estudia': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hace_dinero': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel_educativo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'trabaja_fuera': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.justificacionvbg': {
            'Meta': {'object_name': 'JustificacionVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'justificacion': ('django.db.models.fields.IntegerField', [], {}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'encuesta.lugardetrabajo': {
            'Meta': {'object_name': 'LugarDeTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.motivoparticipacion': {
            'Meta': {'object_name': 'MotivoParticipacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.mujer': {
            'Meta': {'object_name': 'Mujer'},
            'asiste_iglesia': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'comunidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Contraparte']"}),
            'cual_iglesia': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '150', 'blank': 'True'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.Encuestador']"}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lugar_origen': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'encuesta.negociacionexitosa': {
            'Meta': {'object_name': 'NegociacionExitosa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.participacionpublica': {
            'Meta': {'object_name': 'ParticipacionPublica'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'espacio': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Espacio']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.MotivoParticipacion']", 'symmetrical': 'False'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.prevalenciavbg': {
            'Meta': {'object_name': 'PrevalenciaVBG'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'frecuencia': ('django.db.models.fields.IntegerField', [], {}),
            'ha_vivido_vbg': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'que_tipo': ('django.db.models.fields.IntegerField', [], {}),
            'quien': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Quien']", 'symmetrical': 'False'})
        },
        'encuesta.propuesta': {
            'Meta': {'object_name': 'Propuesta'},
            'calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.CalidadAtencion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_porque': ('django.db.models.fields.TextField', [], {}),
            'propuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'si_tipo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'encuesta.propuestanegociada': {
            'Meta': {'object_name': 'PropuestaNegociada'},
            'calidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.CalidadAtencion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_porque': ('django.db.models.fields.TextField', [], {}),
            'propuesta': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'si_tipo': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'encuesta.quedebehacer': {
            'Meta': {'object_name': 'QueDebeHacer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'encuesta.quehaceud': {
            'Meta': {'object_name': 'QueHaceUd'},
            'accionvbg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['encuesta.AccionVBG']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'que_hace': ('django.db.models.fields.IntegerField', [], {})
        },
        'encuesta.quien': {
            'Meta': {'object_name': 'Quien'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.recurso': {
            'Meta': {'object_name': 'Recurso'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'encuesta.resolvervbg': {
            'Meta': {'object_name': 'ResolverVBG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.situacionvbg': {
            'Meta': {'object_name': 'SituacionVBG'},
            'conoce_hombres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'conoce_mujeres': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.solucionconflicto': {
            'Meta': {'object_name': 'SolucionConflicto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'encuesta.tomadecision': {
            'Meta': {'object_name': 'TomaDecision'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'decision': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['encuesta.Decision']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'encuesta.vbg': {
            'Meta': {'object_name': 'VBG'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'encuesta.vivecon': {
            'Meta': {'object_name': 'ViveCon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['encuesta']
